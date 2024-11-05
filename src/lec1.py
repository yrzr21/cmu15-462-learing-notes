import itertools
import matplotlib.pyplot as plt


def draw(u_vals, v_vals):
    # 绘制 2D 投影图
    fig, ax = plt.subplots()

    # 绘制投影后的顶点
    ax.scatter(u_vals, v_vals, color='b')

    # 为每个顶点添加标签
    for i, (u, v) in enumerate(projected_vertices):
        ax.text(u, v, f'P{i + 1}', color='red')

    # 连接投影后的顶点，绘制正方体的边
    edges = [
        (0, 1), (1, 3), (3, 2), (2, 0),  # front face
        (4, 5), (5, 7), (7, 6), (6, 4),  # back face
        (0, 4), (1, 5), (2, 6), (3, 7)  # connecting edges
    ]

    for edge in edges:
        p1, p2 = edge
        ax.plot([u_vals[p1], u_vals[p2]], [v_vals[p1], v_vals[p2]], 'k-', lw=1)

    # 设置坐标轴范围
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # 设置网格，每 1/12 为一个单位
    ax.set_xticks([x / 12 for x in range(0, 13)])  # [0, 1] 范围内的 1/12 格子
    ax.set_yticks([y / 12 for y in range(0, 13)])

    # 启用网格
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)

    # 设置坐标轴标签
    ax.set_xlabel('U (x)')
    ax.set_ylabel('V (y)')
    ax.set_aspect('equal')

    # 显示图形
    plt.show()


# point: xyz, 从xyz，映射到一个垂直于z轴的平面
def convert(point):
    # x轴方向x`=x/z，y轴方向y`=y/z
    u, v = point[0] / point[2], point[1] / point[2]
    print(point, " -> （", u, v, ")")
    return u, v


camera = (2, 3, 5)
vertices = list(itertools.product([-1, 1], repeat=3))
# 平移
vertices = [(x - camera[0], y - camera[1], z - camera[2]) for x, y, z in vertices]
# 投影
projected_vertices = [convert(vertice) for vertice in vertices]

u_vals, v_vals = zip(*projected_vertices)
draw(u_vals, v_vals)




