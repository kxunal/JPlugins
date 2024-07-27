#MIT License

#Copyright (c) 2024 Japanese-X-Userbot

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

try:
    from X.helpers.SQL import BASE, SESSION
except ImportError:
    raise AttributeError

from sqlalchemy import Column, String


class PMPermit(BASE):
    __tablename__ = "pmpermit"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = str(chat_id)  # ensure string


PMPermit.__table__.create(checkfirst=True)


def is_approved(chat_id):
    try:
        return SESSION.query(PMPermit).filter(PMPermit.chat_id == str(chat_id)).one()
    except BaseException:
        return None
    finally:
        SESSION.close()


def approve(chat_id):
    adder = PMPermit(str(chat_id))
    SESSION.add(adder)
    SESSION.commit()


def dissprove(chat_id):
    rem = SESSION.query(PMPermit).get(str(chat_id))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()