import time
import mujoco
import mujoco_viewer

# Give the path to the model's scene.xml file
quadruped = "./models/unitree_a1/scene.xml"
manipulator = "./models/franka_emika_panda/scene.xml"

# Choose which model you want to load
robot_model = quadruped

# Time in seconds
simulation_time = 15


def main():
    model = mujoco.MjModel.from_xml_path(robot_model)
    data = mujoco.MjData(model)

    viewer = mujoco_viewer.MujocoViewer(model, data)

    start = time.time()
    while time.time() - start < simulation_time:

        if viewer.is_alive:
            data.ctrl[0] += 1.0
            mujoco.mj_step(model, data)

            viewer.render()

        else:
            break

    viewer.close()


if __name__ == '__main__':
    main()
