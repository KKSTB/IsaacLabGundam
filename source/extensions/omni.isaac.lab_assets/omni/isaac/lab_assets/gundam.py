import os
import omni.isaac.lab.sim as sim_utils
from omni.isaac.lab.actuators import ImplicitActuatorCfg
from omni.isaac.lab.assets.articulation import ArticulationCfg


GUNDAM_RX78_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        # usd_path=f"omniverse://localhost/Projects/gundam/GGC_TestModel_rx78_20170112_10.usd",
        usd_path=os.path.expanduser('~') + f"/gundam/isaac_lab_gundam_usd/usd/GGC_TestModel_rx78_20170112_10.usd",
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False, solver_position_iteration_count=8, solver_velocity_iteration_count=4
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.18),
        joint_pos={".*": 0.0},
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=0.9,
    actuators={
        "legs": ImplicitActuatorCfg(
            joint_names_expr=[
                ".*leg_crotch_p_joint",
                ".*leg_crotch_r_joint",
                ".*leg_crotch_y_joint",
                ".*leg_knee_p_joint",
                ".*leg_knee_p2_joint",
                "torso_waist_y_joint",
                "torso_waist_p_joint",
                "torso_waist_p2_joint",
            ],
            effort_limit=1000,
            velocity_limit=100.0,
            stiffness={
                ".*leg_crotch_p_joint": 200.0,
                ".*leg_crotch_r_joint": 150.0,
                ".*leg_crotch_y_joint": 150.0,
                ".*leg_knee_p_joint": 200.0,
                ".*leg_knee_p2_joint": 200.0,
                "torso_waist_y_joint": 200.0,
                "torso_waist_p_joint": 200.0,
                "torso_waist_p2_joint": 200.0,
            },
            damping={
                ".*leg_crotch_p_joint": 5.0,
                ".*leg_crotch_r_joint": 5.0,
                ".*leg_crotch_y_joint": 5.0,
                ".*leg_knee_p_joint": 5.0,
                ".*leg_knee_p2_joint": 5.0,
                "torso_waist_y_joint": 5.0,
                "torso_waist_p_joint": 5.0,
                "torso_waist_p2_joint": 5.0,
            },
            # armature={
            #     ".*leg_crotch_p_joint": 0.01,
            #     ".*leg_crotch_r_joint": 0.01,
            #     ".*leg_crotch_y_joint": 0.01,
            #     ".*leg_knee_p_joint": 0.01,
            #     ".*leg_knee_p2_joint": 0.01,
            #     "torso_waist_y_joint": 0.01,
            #     "torso_waist_p_joint": 0.01,
            #     "torso_waist_p2_joint": 0.01,
            # },
        ),
        "feet": ImplicitActuatorCfg(
            joint_names_expr=[".*leg_ankle_p_joint", ".*leg_ankle_r_joint"],
            effort_limit=1000,
            stiffness=20.0,
            damping=1.0,
            # armature=0.01,
        ),
        "arms": ImplicitActuatorCfg(
            joint_names_expr=[
                ".*arm_shoulder_p_joint",
                ".*arm_shoulder_r_joint",
                ".*arm_shoulder_y_joint",
                ".*arm_elbow_p_joint",
                ".*arm_elbow_p2_joint",
                ".*arm_wrist_y_joint",
                ".*arm_wrist_r_joint",
                ".*arm_gripper_joint",
            ],
            effort_limit=1000,
            velocity_limit=100.0,
            stiffness=40.0,
            damping=2.0,
            # armature={
            #     ".*arm_shoulder_p_joint": 0.01,
            #     ".*arm_shoulder_r_joint": 0.01,
            #     ".*arm_shoulder_y_joint": 0.01,
            #     ".*arm_elbow_p_joint": 0.01,
            #     ".*arm_elbow_p2_joint": 0.01,
            #     ".*arm_wrist_y_joint": 0.01,
            #     ".*arm_wrist_r_joint": 0.01,
            #     ".*arm_gripper_joint": 0.001,
            # },
        ),
        "head": ImplicitActuatorCfg(
            joint_names_expr=[
                "head_neck_y_joint",
                "head_neck_p_joint",
            ],
            effort_limit=1000,
            velocity_limit=100.0,
            stiffness=40.0,
            damping=2.0,
            # armature=0.001,
        ),
        "thrust": ImplicitActuatorCfg(
            joint_names_expr=[
                ".*thrust_p_joint",
                ".*thrust_r_joint",
            ],
            effort_limit=1000,
            velocity_limit=100.0,
            stiffness=40.0,
            damping=2.0,
            # armature=0.001,
        ),
    },
)
