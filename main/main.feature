# This project about auto search
Feature: auto Searcher

    Scenario: Presene on Google page home and Search

        Given Launch browser
        When Open Google page
        Then Search about toy
        And close web page
        