import time
import mujoco
import mujoco_viewer

# Give the path to the model's scene.xml file
quadruped = "./models/unitree_a1/scene.xml"
manipulator = "./models/franka_emika_panda/scene.xml"

# Choose which model you want to load
robot_model = quadruped

# Time in seconds
simulation_time = 120


def main():
    """
    This function runs a test simulation and renders it

    :return: void
    """
    # Load model from xml path, and then its data
    model = mujoco.MjModel.from_xml_path(robot_model)
    data = mujoco.MjData(model)

    # Straightens out the back legs to prevent the quadruped from falling
    data.ctrl[7] += 1.0
    data.ctrl[10] += 1.0

    viewer = mujoco_viewer.MujocoViewer(model, data)

    start = time.time()
    while time.time() - start < simulation_time:

        if viewer.is_alive:
            # Run the simulation by 1 step
            mujoco.mj_step(model, data)

            viewer.render()

        else:
            break

    viewer.close()


if __name__ == '__main__':
    main()
