import random

"""
Models the file growth rate of my egr327 with cyclic indexing. Since the project
expects a flat file system, this modification is made to prevent extreme file growth,
as well as ensure constant interaction with other scheduled activities.
"""

step, size = 1, 0
entries = []
last = 0
try:
    # Continue iterating until forcibly canceled via ctrl-C
    while True:
        entries.append(step % 100)
        try:
            entries.remove(random.randint(0, 99))
        except ValueError:
            # Doesn't matter if value not found
            pass
        if step % 10000 == 0:
            print('Size: {0:,} | Step; {1:,} | % of original {2:.3f} | Growth: '
                .format(len(entries), step, 100 * len(entries)/step), len(entries) - last)
            last = len(entries)
        step += 1
except KeyboardInterrupt:
    print('\nSize of {:,} entries after {:,} steps, which is {:.4f}% of the non-cyclic size'
        .format(len(entries), step, 100 * len(entries)/(step - 100)))
