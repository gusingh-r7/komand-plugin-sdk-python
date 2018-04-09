# -*- coding: utf-8 -*-
import sys
import argparse
import komand.message as message
import logging

GREEN = '\033[92m'
RESET = '\033[0m'


class CLI(object):
    """ CLI is a cli for komand """
    def __init__(self, plugin, args=sys.argv[1:]):
        self.plugin = plugin
        self.args = args or []
        self.msg = None

        if "--" in self.args:
            index = self.args.index("--")
            self.msg = " ".join(self.args[index+1:])
            self.args = self.args[:index]

    def test(self, args):
        if args.debug:
            self.plugin.debug = True

        self.plugin.test(self.msg)

    def sample(self, args):
        name = args.name
        trig = self.plugin.triggers.get(name)
        if trig:
            conn = self.plugin.connection
            input = trig.input
            dispatcher = {'url': 'http://localhost:8000', 'webhook_url': ''}

            if conn:
                conn = conn.sample()
            if input:
                input = input.sample()

            msg = message.trigger_start(
                    trigger=trig.name,
                    connection=conn,
                    input=input,
                    dispatcher=dispatcher)

            message.marshal(msg)
            return

        act = self.plugin.actions.get(name)
        if act:
            conn = self.plugin.connection
            input = act.input

            if conn:
                conn = conn.sample()
            if input:
                input = input.sample()

            msg = message.action_start(
                    action=act.name,
                    connection=conn,
                    input=input)

            message.marshal(msg)
            return

        raise ValueError('Invalid trigger or action name.')

    def info(self, args):
        result = ''
        result += 'Name:        %s%s%s\n' % (GREEN, self.plugin.name, RESET)
        result += 'Vendor:      %s%s%s\n' % (GREEN, self.plugin.vendor, RESET)
        result += 'Version:     %s%s%s\n' % (GREEN, self.plugin.version, RESET)
        result += 'Description: %s%s%s\n' % (GREEN, self.plugin.description, RESET)

        if len(self.plugin.triggers) > 0:
            result += '\n'
            result += 'Triggers (%s%d%s): \n' % (GREEN, len(self.plugin.triggers), RESET)

            for name, item in self.plugin.triggers.items():
                result += '└── %s%s%s (%s%s)\n' % (GREEN, name, RESET, item.description, RESET)

        if len(self.plugin.actions) > 0:
            result += '\n'
            result += 'Actions (%s%d%s): \n' % (GREEN, len(self.plugin.actions), RESET)

            for name, item in self.plugin.actions.items():
                result += '└── %s%s%s (%s%s)\n' % (GREEN, name, RESET, item.description, RESET)

        print(result)

    def _run(self, args):
        if args.debug:
            self.plugin.debug = True

        self.plugin.run(self.msg)

    def run(self):
        """Run the CLI tool"""
        parser = argparse.ArgumentParser(description=self.plugin.description)
        parser.add_argument('--version', action='store_true', help='Show version', default=False)
        parser.add_argument('--debug', action='store_true', help='Log events to stdout', default=False)

        subparsers = parser.add_subparsers(help='Commands')

        test_command = subparsers.add_parser('test', help='Run a test using the start message on stdin')
        test_command.set_defaults(func=self.test)

        info_command = subparsers.add_parser('info', help='Display plugin info (triggers and actions).')
        info_command.set_defaults(func=self.info)

        sample_command = subparsers.add_parser('sample',
                                               help='Show a sample start message for the provided trigger or action.')
        sample_command.add_argument('name', help='trigger or action name')
        sample_command.set_defaults(func=self.sample)

        run_command = subparsers.add_parser('run',
                                            help='Run the plugin (default command).'
                                                 'You must supply the start message on stdin.')
        run_command.set_defaults(func=self._run)

        args = parser.parse_args(self.args)

        if args.debug:
            logging.basicConfig(level=logging.DEBUG)
        else:
            logging.basicConfig(level=logging.INFO)

        if not hasattr(args, 'func') or not args.func:
            return parser.print_help()

        args.func(args)
