from sys import stdin

def parse_input():
    file_prefix = next(stdin).strip()

    states = []
    for line in stdin:
        states.append(line.strip())
    return file_prefix, states

def prepare_header(name, states):
    res  = "extern const char* " + name.upper() + "_names[];\n"
    res += "typedef enum {\n"
    for state in states:
        res += "  " + state + ",\n"
    res += "} " + name.upper() + ";\n"
    return res

def prepare_c(name, states):
    res  = "const char* " + name.upper() + "_names[] = {\n"
    res += "  "
    for state in states:
        res += "\"" + state + "\", "
    res = res[:-2]
    res += "\n};\n"
    return res

def writeout(prefix, extension, contents):
    f = open(prefix + extension, "w")
    f.write(contents)

file_prefix, states = parse_input()
writeout(file_prefix, ".c", prepare_c(file_prefix, states))
writeout(file_prefix, ".h", prepare_header(file_prefix, states))
