# with open('test.txt', 'r') as f:
#     size_to_read = 10

#     f_contents = f.read(size_to_read)
#     print(f.tell())

#     # while len(f_contents)> 0:
#     #     print(f_contents, end="*")
#     #     f_contents = f.read(size_to_read)

# with open('test.txt', 'r') as rf:
#     with open('test_copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)

with open("cute_puppy.jpg", "rb") as rf:
    with open("cute_puppy_copy.jpg", "wb") as wf:
        for line in rf:
            wf.write(line)
