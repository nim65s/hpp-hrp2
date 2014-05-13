#!/usr/bin/env python
# Copyright (c) 2014 CNRS
# Author: Florent Lamiraux
#
# This file is part of hpp-corbaserver.
# hpp-corbaserver is free software: you can redistribute it
# and/or modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation, either version
# 3 of the License, or (at your option) any later version.
#
# hpp-corbaserver is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Lesser Public License for more details.  You should have
# received a copy of the GNU Lesser General Public License along with
# hpp-corbaserver.  If not, see
# <http://www.gnu.org/licenses/>.

from hpp.corbaserver.manipulation.robot import Robot as Parent

class Robot (Parent):
    packageName = "hrp2_14_description"
    urdfName = "hrp2_14"
    urdfSuffix = ""
    srdfSuffix = ""
    halfSitting = \
        {"base_joint_x": 0.0,
         "base_joint_y": 0.0,
         "base_joint_z": 0.648702,
         "base_joint_SO3": (1.0, 0.0, 0.0, 0.0),
         "CHEST_JOINT0": 0.0,
         "CHEST_JOINT1": 0.0,
         "HEAD_JOINT0": 0.0,
         "HEAD_JOINT1": 0.0,
         "LARM_JOINT0": 0.261799,
         "LARM_JOINT1": 0.17453,
         "LARM_JOINT2": 0.0,
         "LARM_JOINT3": -0.523599,
         "LARM_JOINT4": 0.0,
         "LARM_JOINT5": 0.0,
         "LARM_JOINT6": 0.1,
         "LHAND_JOINT0": 0.0,
         "LHAND_JOINT1": 0.0,
         "LHAND_JOINT2": 0.0,
         "LHAND_JOINT3": 0.0,
         "LHAND_JOINT4": 0.0,
         "RARM_JOINT0": 0.261799,
         "RARM_JOINT1": -0.17453,
         "RARM_JOINT2": 0.0,
         "RARM_JOINT3": -0.523599,
         "RARM_JOINT4": 0.0,
         "RARM_JOINT5": 0.0,
         "RARM_JOINT6": 0.1,
         "RHAND_JOINT0": 0.0,
         "RHAND_JOINT1": 0.0,
         "RHAND_JOINT2": 0.0,
         "RHAND_JOINT3": 0.0,
         "RHAND_JOINT4": 0.0,
         "LLEG_JOINT0": 0.0,
         "LLEG_JOINT1": 0.0,
         "LLEG_JOINT2": -0.453786,
         "LLEG_JOINT3": 0.872665,
         "LLEG_JOINT4": -0.418879,
         "LLEG_JOINT5": 0.0,
         "RLEG_JOINT0": 0.0,
         "RLEG_JOINT1": 0.0,
         "RLEG_JOINT2": -0.453786,
         "RLEG_JOINT3": 0.872665,
         "RLEG_JOINT4": -0.418879,
         "RLEG_JOINT5": 0.0
         }

    def __init__ (self, robotName):
        Parent.__init__ (self, robotName, "freeflyer")
        hs = self.halfSitting.copy ()
        for joint, value in hs.iteritems ():
            self.halfSitting [self.robotName + "/" + joint] = value
        self.rightWrist = self.robotName + "/RARM_JOINT5"
        self.leftWrist  = self.robotName + "/LARM_JOINT5"
        self.rightAnkle = self.robotName + "/RLEG_JOINT5"
        self.leftAnkle  = self.robotName + "/LLEG_JOINT5"
        self.waist = self.robotName + "/base_joint_SO3"
        self.chest = self.robotName + "/CHEST_JOINT1"
        self.gaze = self.robotName + "/HEAD_JOINT1"

    def getInitialConfig (self):
        q = []
        for n in self.jointNames:
            if self.halfSitting.has_key (n):
                dof = self.halfSitting [n]
                if type (dof) is tuple:
                    q += dof
                else:
                    q.append (dof)
            else:
                size = self.client.basic.robot.getJointConfigSize (n)
                q += size * [None,]
        return q

    def leftHandClosed (self) :
        dofs = {self.robotName + "/LARM_JOINT6": 0.1,
                self.robotName + "/LHAND_JOINT0": 0.0,
                self.robotName + "/LHAND_JOINT1": 0.0,
                self.robotName + "/LHAND_JOINT2": 0.0,
                self.robotName + "/LHAND_JOINT3": 0.0,
                self.robotName + "/LHAND_JOINT4": 0.0}
        return dofs

    def rightHandClosed (self) :
        dofs = {self.robotName + "/RARM_JOINT6": 0.1,
                self.robotName + "/RHAND_JOINT0": 0.0,
                self.robotName + "/RHAND_JOINT1": 0.0,
                self.robotName + "/RHAND_JOINT2": 0.0,
                self.robotName + "/RHAND_JOINT3": 0.0,
                self.robotName + "/RHAND_JOINT4": 0.0}
        return dofs