#!/bin/python
# I make the assumption that I can arbitrarily select "body", "leg_L" and "leg_R" in this script. Need to go through
# and make it so that I select from a subset of the current selection only.
# TODO: Pass the currently selected object as a parameter and select Body, and Legs as a subset of that
import maya.cmds as mc


def run_end():
    animation_time = 6
    start_animation_time = mc.currentTime(query=True)
    end_animation_time = start_animation_time + animation_time

    # Global Movements: Leaning the body forward and translating it forward
    mc.select("body")
    mc.move(0, 0, 1, r=True)
    mc.setKeyframe(at="translateZ", time=end_animation_time)
    mc.rotate(0, 0, 0)
    mc.setKeyframe(at="rotateX", time=end_animation_time)

    # Rotate Legs AND SCALE LEGS
    # Rotate legA (x) forward 35
    # Rotate legB (x) backward -35
    mc.select("leg_R")
    mc.rotate(0, 0, 0)
    mc.setKeyframe(at="rotateX", time=end_animation_time)
    mc.select("leg_L")
    mc.rotate(0, 0, 0)
    mc.setKeyframe(at="rotateX", time=end_animation_time)
    mc.currentTime(end_animation_time)

run_end()