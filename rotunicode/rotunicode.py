# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import codecs
import strop


class RotUnicode(codecs.Codec):
    """
    Codec for converting between a string of ASCII and Unicode chars
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

    _ascii_alphabet = strop.lowercase + strop.uppercase + '0123456789'
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

    def encode(self, string, errors='strict'):
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
            raise UnicodeError('Unsupported error handling {}'.format(errors))

        unicode_string = self._ensure_unicode_string(string)
        encoded = unicode_string.translate(self._encoding_table)
        return encoded, len(string)

    def decode(self, string, errors='strict'):
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
            raise UnicodeError('Unsupported error handling {}'.format(errors))

        unicode_string = self._ensure_unicode_string(string)
        decoded = unicode_string.translate(self._decoding_table)
        return decoded, len(string)

    @classmethod
    def search_function(cls, encoding):
        """Search function to find 'rotunicode' codec."""
        if encoding == cls._codec_name:
            return codecs.CodecInfo(
                name=cls._codec_name,
                encode=RotUnicode().encode,
                decode=RotUnicode().decode,
            )
        return None

    @classmethod
    def _ensure_unicode_string(cls, string):
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
        if not isinstance(string, unicode):
            string = string.decode('utf-8')
        return string
