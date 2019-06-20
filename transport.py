import xml.etree.ElementTree as ET
import os


dump_attributes = False


def unhandledTag(tag: str):
    print('Unhandled tag [{}]'.format(tag))


def handleInputType(elem: ET.Element):
    pass


def handleTool(elem: ET.Element):
    name = elem.attrib['name']
    # value = elem.attrib['value']
    # valtype = elem.attrib['valueType']

    # print('---- option tool [{}] Name [{}] ----'.format(elem.tag, name))

    if dump_attributes:
        for attr in elem.attrib:
            print('Attribute {} - {}'.format(attr, elem.attrib[attr]))

    for child in elem:
        if child.tag == 'option':
            handleOption(child)
        elif child.tag == 'inputType':
            handleInputType(child)
        else:
            unhandledTag(child.tag)

    # print('---- END tool ----')


def handleTargetPlatform(elem: ET.Element):
    # name = elem.attrib['name']
    # value = elem.attrib['value']
    # valtype = elem.attrib['valueType']

    # print('---- option targetPlatform [{}] Name [{}] ----'.format(elem.tag, None))

    if dump_attributes:
        for attr in elem.attrib:
            print('Attribute {} - {}'.format(attr, elem.attrib[attr]))

    # for child in elem:
    #     print('Child tag {}'.format(child.tag))

    # print('---- END targetPlatform ----')


def handleBuilder(elem: ET.Element):
    # name = elem.attrib['name']
    # value = elem.attrib['value']
    # valtype = elem.attrib['valueType']

    # print('---- option builder [{}] Name [{}] ----'.format(elem.tag, None))

    if dump_attributes:
        for attr in elem.attrib:
            print('Attribute {} - {}'.format(attr, elem.attrib[attr]))

    for child in elem:
        print('Child tag {}'.format(child.tag))

    # print('---- END builder ----')


def handleListOptionValue(elem: ET.Element, valtype: str):
    # print('---- option listOptionValue [{}] Name [{}] ----'.format(elem.tag, None))
    builtIn = elem.attrib['builtIn']
    value = elem.attrib['value']

    if dump_attributes:
        for attr in elem.attrib:
            print('Attribute {} - {}'.format(attr, elem.attrib[attr]))

    if valtype == 'definedSymbols':
        print('{}'.format(value))
    elif valtype == 'includePath':
        oldpath = elem.attrib['value']
        path = oldpath.replace('\\', '/')
        elem.attrib['value'] = path
        print('Modified path {} -> {}'.format(oldpath, path))

    # for child in elem:
    #     print('Child tag {}'.format(child.tag))

    # print('---- END listOptionValue ----')


# def handleIncludePath(elem: ET.Element):
#     builtin = elem.attrib['builtIn']
#     value = elem.attrib['value']
#
#     # print('Modify include path builtIn : {} value : {}'.format(builtin, value))
#
#     oldpath = elem.attrib['value']
#     path = oldpath.replace('\\', '/')
#     elem.attrib['value'] = path
#
#     print('Modified path {} -> {}'.format(oldpath, path))


def handleOption(elem: ET.Element):
    name = elem.attrib['name']
    value = None
    valtype = None

    if 'value' in elem.attrib:
        value = elem.attrib['value']
    if 'valueType' in elem.attrib:
        valtype = elem.attrib['valueType']

    # print('---- option Tag [{}] Name [{}] ----'.format(elem.tag, name))

    # print('NAME : {} VALUE {} TYPE {}'.format(name, value, valtype))

    if dump_attributes:
        for attr in elem.attrib:
            print('Attribute {} - {}'.format(attr, elem.attrib[attr]))

    for child in elem:
        if child.tag == 'listOptionValue':
            handleListOptionValue(child, valtype)
            # if valtype == 'includePath':
            #     handleIncludePath(child)
            # else:
            #     handleListOptionValue(child)
        else:
            unhandledTag(child.tag)

    # print('---- END option ----')


def handleToolChain(elem: ET.Element):
    name = elem.attrib['name']

    # print('---- toolChain Tag [{}] Name [{}] ----'.format(elem.tag, name))

    if dump_attributes:
        for attr in elem.attrib:
            print('Attribute {} - {}'.format(attr, elem.attrib[attr]))

    for child in elem:
        # print('Child : {}'.format(child.tag))

        if child.tag == 'option':
            handleOption(child)
        elif child.tag == 'targetPlatform':
            handleTargetPlatform(child)
        elif child.tag == 'builder':
            handleBuilder(child)
        elif child.tag == 'tool':
            handleTool(child)
        else:
            unhandledTag(child.tag)

    # print('---- END toolChain ----')


def handleEntry(elem: ET.Element):
    name = elem.attrib['name']

    # print('---- entry Tag [{}] ----'.format(elem.tag, name))

    if dump_attributes:
        for attr in elem.attrib:
            print('Attribute {} - {}'.format(attr, elem.attrib[attr]))

    for child in elem:
        print('Child tag {}'.format(child.tag))

    # print('---- END entry ----')


def handleSourceEntries(elem: ET.Element):
    # print('---- sourceEntries Tag [{}] Name [{}]----'.format(elem.tag, None))

    if dump_attributes:
        for attr in elem.attrib:
            print('Attribute {} - {}'.format(attr, elem.attrib[attr]))

    for child in elem:
        if child.tag == 'entry':
            handleEntry(child)
        else:
            unhandledTag(child.tag)

    # print('---- END sourceEntries ----')


def handleFolderInfo(elem: ET.Element):
    name = elem.attrib['name']

    # print('---- FolderInfo Tag [{}] Name [{}] ----'.format(elem.tag, name))

    if dump_attributes:
        for attr in elem.attrib:
            print('Attribute {} - {}'.format(attr, elem.attrib[attr]))

    for child in elem:
        if child.tag == 'toolChain':
            handleToolChain(child)
        else:
            unhandledTag(child.tag)

    # print('---- END FolderInfo ----')


def handleConfiguration(elem: ET.Element):
    name = None
    if 'name' is elem.attrib:
        name = elem.attrib['name']
    elif 'configurationName' in elem.attrib:
        name = elem.attrib['configurationName']

    # name = elem.attrib['name']
    # print('---- Tag {} Name {}----'.format(elem.tag, name))
    print('Found build target {}'.format(name))

    if dump_attributes:
        for attr in elem.attrib:
            print('Attribute {} - {}'.format(attr, elem.attrib[attr]))

    for child in elem:
        # print('Child tag {}'.format(child.tag))
        if child.tag == 'folderInfo':
            handleFolderInfo(child)
        elif child.tag == 'sourceEntries':
            handleSourceEntries(child)
        else:
            unhandledTag(child.tag)

    # print('---- END Configuration ----')


def handleExternalSettings(elem: ET.Element):
    # print('---- CONFIGURATION Tag {} ----'.format(elem.tag))
    return


def handleExtensions(elem: ET.Element):
    # print('---- Tag {} ----'.format(elem.tag))
    #
    # for extension in elem:
    #     extId = extension.attrib['id']
    #     point = extension.attrib['point']
    #     print('Extension id {} point {}'.format(extId, point))
    return


def handleEmbeddedStorageModule(elem: ET.Element):
    # print('---- Tag {} ----'.format(elem.tag))

    moduleId = elem.attrib['moduleId']
    versionNum = None
    name = None

    if 'name' in elem.attrib:
        name = elem.attrib['name']

    if 'version' in elem.attrib:
        versionNum = elem.attrib['version']
    elif 'versionNum' in elem.attrib:
        versionNum = elem.attrib['versionNum']

    # print('Module ID : {} Version {} Name {}'.format(moduleId, versionNum, name))

    if dump_attributes:
        for attr in elem.attrib:
            print('Attribute {} - {}'.format(attr, elem.attrib[attr]))

    for child in elem:
        # print('--- embedded storage module tag {} ---'.format(child.tag))
        if child.tag == 'externalSettings':
            handleExternalSettings(child)
        elif child.tag == 'extensions':
            handleExtensions(child)
        elif child.tag == 'configuration':
            handleConfiguration(child)
        else:
            unhandledTag(child.tag)


def handleCconfiguration(elem: ET.Element):
    id = elem.attrib['id']

    # print('---- cconfiguration Tag {} Id {} ----'.format(elem.tag, id))

    if dump_attributes:
        for attr in elem.attrib:
            print('Attribute {} - {}'.format(attr, elem.attrib[attr]))

    for child in elem:
        if child.tag == 'storageModule':
            handleEmbeddedStorageModule(child)
        else:
            pass
        # print(child.tag)

    # print('---- END cconfiguration ----')


def handleProject(elem: ET.Element):
    return


def handleStorageModule(elem : ET.Element):
    # print('---- Tag {} ----'.format(elem.tag))

    moduleId = elem.attrib['moduleId']
    versionNum = None

    if 'version' in elem.attrib:
        versionNum = elem.attrib['version']
    elif 'versionNum' in elem.attrib:
        versionNum = elem.attrib['versionNum']

    # print('Module ID : {} Version {}'.format(moduleId, versionNum))

    if dump_attributes:
        for attr in elem.attrib:
            print('Attribute {} - {}'.format(attr, elem.attrib[attr]))

    # Iterate through children
    for child in elem:
        # print(child.tag)
        if child.tag == "cconfiguration":
            handleCconfiguration(child)
        elif child.tag == 'configuration':
            handleConfiguration(child)
        elif child.tag == 'project':
            handleProject(child)
        else:
            unhandledTag(child.tag)


def convertProject(input_file: str, output_file: str) -> bool:

    if not os.path.exists(input_file):
        print('Input file does not exist...')
        return False

    tree = ET.parse(input_file)
    root = tree.getroot()

    # print("Root element = {}".format(root.tag))

    for elem in root:
        if elem.tag == "storageModule":
            handleStorageModule(elem)
        else:
            print('ERROR: Does not appear to be a project file!')
            return False

    tree.write(output_file)
    return True


def doConversion():
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('--input',  '-i', default='.cproject')
    parser.add_argument('--output', '-o', default='.cproject.new')
    parser.add_argument('--debug', '-d')

    options = parser.parse_args()

    convertProject(options.input, options.output)


if __name__ == '__main__':
    doConversion()
