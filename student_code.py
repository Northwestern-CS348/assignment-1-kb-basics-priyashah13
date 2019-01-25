import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        """Assert a fact or rule into the KB


        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py

        check if fact is an instance of Fact - if it is, then append fact
        """
        print("Asserting {!r}".format(fact))
        if factq(fact.name):
            self.facts.append(fact)

        
    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise

        get all the bindings using the listofbindings class
        for every fact in knowledge base, match
        if match is not false, add match to bindings list

        if the list of bindings is empty, return false
        else, return the list of bindings

        """
        print("Asking {!r}".format(fact))
        bindings = ListOfBindings()
        if(isinstance(fact, Fact)):
            for x in self.facts:
                m = match(fact.statement, x.statement)
                if (m != False):
                    bindings.add_bindings(m)
        if len(bindings) == 0:
            return False
        else:
            return bindings

