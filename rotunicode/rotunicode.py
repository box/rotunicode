# coding: utf-8

from __future__ import unicode_literals
import codecs
import six


class RotUnicode(codecs.Codec):
    """
    Codec for converting between a string of ASCII and non-ASCII chars
    maintaining readability.

    >>> codes.register(RotUnicode.search_function)
    >>> 'Hello Frodo!'.encode('rotunicode')
    Ĥȅľľő Ƒŕőďő!
    >>> 'Ĥȅľľő Ƒŕőďő!'.decode('rotunicode')
    Hello Frodo!

    RotUnicode stands for rotate-to-unicode. Or rotten-unicode for those who
    have nightmares about Unicode. It was inspired by Rot13.
    """
    # pylint: disable=no-init
    # The base class does not define it.

    _codec_name = 'rotunicode'

    _lowercase = 'abcdefghijklmnopqrstuvwxyz'
    _uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    _ascii_alphabet = _lowercase + _uppercase + '0123456789'
    _rot_unicode_alphabet = ('ȁƄćďȅƒġĥȉĵƙľḿńőҏqŕŝƭȕѵŵхŷż' +
                             'ȀβĆĎȄƑĜĤȈĴƘĽḾŃŐΡɊŔŜƬȔѴŴΧŶŻ' +
                             'Ꮎ➀➁➂➃➄➅➆➇➈')

    _encoding_table = dict(
        zip(
            (ord(c) for c in _ascii_alphabet),
            _rot_unicode_alphabet,
        ),
    )

    _decoding_table = dict(
        zip(
            (ord(c) for c in _rot_unicode_alphabet),
            (ord(c) for c in _ascii_alphabet),
        ),
    )

    # pylint:disable=arguments-differ
    @classmethod
    def encode(cls, string, errors='strict'):
        """Return the encoded version of a string.

        :param string:
            The input string to encode.
        :type string:
            `basestring`

        :param errors:
            The error handling scheme. Only 'strict' is supported.
        :type errors:
            `basestring`

        :return:
            Tuple of encoded string and number of input bytes consumed.
        :rtype:
            `tuple` (`unicode`, `int`)
        """
        if errors != 'strict':
            raise UnicodeError('Unsupported error handling {0}'.format(errors))

        unicode_string = cls._ensure_unicode_string(string)
        encoded = unicode_string.translate(cls._encoding_table)
        return encoded, len(string)

    @classmethod
    def decode(cls, string, errors='strict'):
        """Return the decoded version of a string.

        :param string:
            The input string to decode.
        :type string:
            `basestring`

        :param errors:
            The error handling scheme. Only 'strict' is supported.
        :type errors:
            `basestring`

        :return:
            Tuple of decoded string and number of input bytes consumed.
        :rtype:
            `tuple` (`unicode`, `int`)
        """
        if errors != 'strict':
            raise UnicodeError('Unsupported error handling {0}'.format(errors))

        unicode_string = cls._ensure_unicode_string(string)
        decoded = unicode_string.translate(cls._decoding_table)
        return decoded, len(string)
    # pylint:enable=arguments-differ

    @classmethod
    def search_function(cls, encoding):
        """Search function to find 'rotunicode' codec."""
        if encoding == cls._codec_name:
            return codecs.CodecInfo(
                name=cls._codec_name,
                encode=cls.encode,
                decode=cls.decode,
            )
        return None

    @staticmethod
    def _ensure_unicode_string(string):
        """Returns a unicode string for string.

        :param string:
            The input string.
        :type string:
            `basestring`

        :returns:
            A unicode string.
        :rtype:
            `unicode`
        """
        if not isinstance(string, six.text_type):
            string = string.decode('utf-8')
        return string
