# -*- coding: utf-8 -*-
# Copyright (C) 2006-2007 Søren Roug, European Environment Agency
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
#
# Contributor(s):
#

from .namespaces import METANS
from .element import Element

# Autogenerated


def AutoReload(**args):
    return Element(qname=(METANS, 'auto-reload'), **args)


def CreationDate(**args):
    return Element(qname=(METANS, 'creation-date'), **args)


def DateString(**args):
    return Element(qname=(METANS, 'date-string'), **args)


def DocumentStatistic(**args):
    return Element(qname=(METANS, 'document-statistic'), **args)


def EditingCycles(**args):
    return Element(qname=(METANS, 'editing-cycles'), **args)


def EditingDuration(**args):
    return Element(qname=(METANS, 'editing-duration'), **args)


def Generator(**args):
    return Element(qname=(METANS, 'generator'), **args)


def HyperlinkBehaviour(**args):
    return Element(qname=(METANS, 'hyperlink-behaviour'), **args)


def InitialCreator(**args):
    return Element(qname=(METANS, 'initial-creator'), **args)


def Keyword(**args):
    return Element(qname=(METANS, 'keyword'), **args)


def PrintDate(**args):
    return Element(qname=(METANS, 'print-date'), **args)


def PrintedBy(**args):
    return Element(qname=(METANS, 'printed-by'), **args)


def Template(**args):
    return Element(qname=(METANS, 'template'), **args)


def UserDefined(**args):
    return Element(qname=(METANS, 'user-defined'), **args)
