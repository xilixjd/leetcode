# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''
TinyURL是一种URL简化服务， 比如：当你输入一个URL https://leetcode.com/problems/design-tinyurl 时，
它将返回一个简化的URL http://tinyurl.com/4e9iAk.

要求：设计一个 TinyURL 的加密 encode 和解密 decode 的方法。你的加密和解密算法如何设计和运作是没有限制的，
你只需要保证一个URL可以被加密成一个TinyURL，并且这个TinyURL可以用解密方法恢复成原本的URL。
'''


class Codec:
    def __init__(self):
        self.counter = 1
        self.map = {}
        self.demap = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        if self.map.get(longUrl) is None:
            tiny_url = "http://tinyurl.com/" + str(self.counter)
            self.demap[tiny_url] = longUrl
            self.map[longUrl] = tiny_url
            self.counter += 1
            return tiny_url
        else:
            return self.map[longUrl]

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.demap[shortUrl]


# Your Codec object will be instantiated and called as such:
codec = Codec()
d = codec.encode("https://leetcode.com/problems/design-tinyurl")
print codec.decode(d)