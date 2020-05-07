import sys, os
sys.path.append("../src")

from tailtrim import TailTrimmer

filename = "sample.txt"
filename_tmp = "sample.txt.swp"

def init_single_file():
    with open(filename, "w") as f:
        f.write("Test  \n")
        f.write("Test\n")
        f.write("\n")
        f.write(" \n")
        f.write(" abac ")

def file_trim_with_lf():
    # Create the first file
    init_single_file()

    # Trim it
    trimmer = TailTrimmer(use_crlf=False)
    trimmer.trim_file(filename)

    # Assert correctness
    filetext = None
    with open(filename, "rb") as f:
        filetext = f.read().decode('ascii')
    assert filetext == "Test\nTest\n\n\n abac\n"

    # Cleanup
    os.remove(filename)

def file_trim_with_crlf_with_swap():
    # Create the first file
    init_single_file()
    # Copy the file to the swap file
    os.system(f"cp {filename} {filename_tmp}")

    # Trim using a swap file and use CRLF endings
    # Trimming with the swap file means that
    # not all of the file will be loaded into memory at once
    trimmer = TailTrimmer(use_crlf=True)
    trimmer.trim_file(filename, filename_tmp)

    # Assert correctness
    filetext = None
    with open(filename, "rb") as f:
        filetext = f.read().decode('ascii')
    assert filetext == "Test\r\nTest\r\n\r\n\r\n abac\r\n"

    # Cleanup
    os.remove(filename)
    os.remove(filename_tmp)

def main():
    file_trim_with_lf()
    file_trim_with_crlf_with_swap()
    print("All asserts passed!")

if __name__ == "__main__":
    main()
