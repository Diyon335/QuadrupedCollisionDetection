import mujoco
from mujoco import viewer


def main():
    model = mujoco.MjModel.from_xml_path("./models/unitree_a1/scene.xml")
    data = mujoco.MjData(model)
    viewer.launch(model, data)


if __name__ == '__main__':
    main()
