def math_operations(*floats, **kwargs):
    keys = list(kwargs.keys())
    for i in range(len(floats)):
        key = keys[i % 4]
        if key == "a":
            kwargs[key] += floats[i]
        elif key == "s":
            kwargs[key] -= floats[i]
        elif key == "d":
            if floats[i] != 0:
                kwargs[key] /= floats[i]
        elif key == "m":
            kwargs[key] *= floats[i]

    sorted_kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))

    return "\n".join(f"{k}: {v:.1f}" for k, v in sorted_kwargs)

print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
