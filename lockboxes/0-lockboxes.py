#!/usr/bin/python3
"""
Module 0-lockboxes
Contains a method to determine if all locked boxes can be opened.
"""


def canUnlockAll(boxes):
    """Determines if all boxes can be opened."""
    boites_ouvertes = set([0])
    cles_a_verifier = [0]

    while cles_a_verifier:
        boite_actuelle = cles_a_verifier.pop()
        for cle in boxes[boite_actuelle]:
            if cle not in boites_ouvertes:
                boites_ouvertes.add(cle)
                cles_a_verifier.append(cle)
    return len(boites_ouvertes) == len(boxes)
