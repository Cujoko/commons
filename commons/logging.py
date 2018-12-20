# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# noinspection PyUnresolvedReferences
import logging


def add_logging_arguments(parser):
    parser.add_argument(
        '-l', '--level',
        nargs='?',
        help='Set log\'s level'
    )
    parser.add_argument(
        '--log-file',
        nargs='?',
        help='Set log file'
    )
    parser.add_argument(
        '--log-file-level',
        nargs='?',
        help='Set log file\'s level'
    )


def add_loggers(args, main_logger):
    # noinspection PyUnresolvedReferences
    formatter = logging.Formatter(
        '[%(asctime)s,%(msecs)03d][%(name)s:%(lineno)d][%(levelname)s] %(message)s',
        datefmt='%y-%m-%d %H:%M:%S')
    if args.level is not None:
        level_str = args.level
    else:
        level_str = 'INFO'
    level_str = level_str.upper()
    level_int = getattr(logging, level_str, None)
    if not isinstance(level_int, int):
        raise ValueError('Invalid log level \'{0}\''.format(level_str))
    # noinspection PyUnresolvedReferences
    ch = logging.StreamHandler()
    ch.setLevel(level_int)
    ch.setFormatter(formatter)
    main_logger.addHandler(ch)
    if args.log_file is not None:
        log_file_fullname = args.log_file
        if args.log_file_level is not None:
            log_file_level_str = args.log_file_level
        else:
            log_file_level_str = 'INFO'
        log_file_level_str = log_file_level_str.upper()
        log_file_level_int = getattr(logging, log_file_level_str, None)
        if not isinstance(log_file_level_int, int):
            raise ValueError('Invalid log file level \'{0}\''.format(log_file_level_str))
        # noinspection PyUnresolvedReferences
        fh = logging.FileHandler(log_file_fullname)
        fh.setLevel(log_file_level_int)
        fh.setFormatter(formatter)
        main_logger.addHandler(fh)