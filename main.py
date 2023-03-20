import time
import mujoco
from mujoco import viewer

# Give the path to the model's scene.xml file
quadruped = "./models/unitree_a1/scene.xml"
manipulator = "./models/franka_emika_panda/scene.xml"

# Choose which model you want to load
robot_model = quadruped


def main():
    model = mujoco.MjModel.from_xml_path(robot_model)

    data = mujoco.MjData(model)

    renderer = mujoco.Renderer(model)

    context = mujoco.GLContext(900, 800)
    context.make_current()

    start = time.time()
    while time.time() - start < 5:

        data.ctrl[0] += 1.0
        mujoco.mj_step(model, data)

        renderer.update_scene(data)

    renderer.render()


if __name__ == '__main__':
    main()
