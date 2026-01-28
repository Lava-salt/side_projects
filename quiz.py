print("Quiz Game\n\nMultiplayer quiz game about programming and animals for (an intellectual) family('s) fun!")
what = int(input("1 - [Programming Quiz]\n2 - [Animals Quiz]\n3 - [All Quiz]\n\n"))

# Sources: Python modules and Dwarf Fortress files

from math import e, pi, tau
from sys import *
from time import *
from datetime import UTC
from calendar import *
from random import randint

q = []
a = []

def addq(x, y):
    q.append(x)
    a.append(y)

if what == 1 or what == 3:

    addq("What is e?", e)
    addq("What is pi?", pi)
    addq("What is tau?", tau)

    x = """exec_prefix -- prefix used to find the machine-specific Python library
        executable -- absolute path of the executable binary of the Python interpreter
        float_repr_style -- string indicating the style of repr() output for floats
        hexversion -- version information encoded as a single integer
        maxsize -- the largest supported length of containers.
        maxunicode -- the value of the largest Unicode code point
        platform -- platform identifier
        prefix -- prefix used to find the Python library
        thread_info -- a named tuple with information about the thread implementation.
        version -- the version of this interpreter as a string
        version_info -- version information as a named tuple
        dllhandle -- integer handle of the Python DLL
        winver -- version number of the Python DLL
        displayhook -- called to show results in an interactive session
        excepthook -- called to handle any uncaught exception other than SystemExit""".split("\n")
    for i in x:
        j = i.split("--")
        addq(f"What is {j[1].strip().strip("; don't touch!").strip(".")}?", eval(j[0].strip()))

    """altzone = -14400
        daylight = 0
        timezone = -10800
        tzname = ('Russia TZ 2 Standard Time', 'Russia TZ 2 Summer Time')"""

    addq("What is the altitude zone?", altzone)
    addq("What is the amount of daylight?", daylight)
    addq("What is the time zone?", timezone)
    addq("What is the time zone name?", tzname[0])

    x = """APRIL = calendar.APRIL
        AUGUST = calendar.AUGUST
        DECEMBER = calendar.DECEMBER
        FEBRUARY = calendar.FEBRUARY
        FRIDAY = calendar.FRIDAY
        JANUARY = calendar.JANUARY
        JULY = calendar.JULY
        JUNE = calendar.JUNE
        MARCH = calendar.MARCH
        MAY = calendar.MAY
        MONDAY = calendar.MONDAY
        NOVEMBER = calendar.NOVEMBER
        OCTOBER = calendar.OCTOBER
        SATURDAY = calendar.SATURDAY
        SEPTEMBER = calendar.SEPTEMBER
        SUNDAY = calendar.SUNDAY
        THURSDAY = calendar.THURSDAY
        TUESDAY = calendar.TUESDAY
        WEDNESDAY = calendar.WEDNESDAY""".split("\n")
    for i in x:
        j = i.split("=")[0].strip()
        if j[::-1][:3] == "YAD":
            addq(f"Which day of the week no. is {j.capitalize()}?", eval(j) + 1)
        else:
            addq(f"Which day of the month no. is {j.capitalize()}?", eval(j))

    x = """ASSOC          Displays or modifies file extension associations.
    ATTRIB         Displays or changes file attributes.
    BREAK          Sets or clears extended CTRL+C checking.
    BCDEDIT        Sets properties in boot database to control boot loading.
    CACLS          Displays or modifies access control lists (ACLs) of files.
    CALL           Calls one batch program from another.
    CD             Displays the name of or changes the current directory.
    CHCP           Displays or sets the active code page number.
    CHDIR          Displays the name of or changes the current directory.
    CHKDSK         Checks a disk and displays a status report.
    CHKNTFS        Displays or modifies the checking of disk at boot time.
    CLS            Clears the screen.
    CMD            Starts a new instance of the Windows command interpreter.
    COLOR          Sets the default console foreground and background colors.
    COMP           Compares the contents of two files or sets of files.
    COMPACT        Displays or alters the compression of files on NTFS partitions.
    CONVERT        Converts FAT volumes to NTFS. You cannot convert the current drive.
    COPY           Copies one or more files to another location.
    DATE           Displays or sets the date.
    DEL            Deletes one or more files.
    DIR            Displays a list of files and subdirectories in a directory.
    DISKPART       Displays or configures Disk Partition properties.
    DOSKEY         Edits command lines, recalls Windows commands, and creates macros.
    DRIVERQUERY    Displays current device driver status and properties.
    ECHO           Displays messages, or turns command echoing on or off.
    ENDLOCAL       Ends localization of environment changes in a batch file.
    ERASE          Deletes one or more files.
    EXIT           Quits the CMD.EXE program (command interpreter).
    FC             Compares two files or sets of files, and displays the differences between them.
    FIND           Searches for a text string in a file or files.
    FINDSTR        Searches for strings in files.
    FOR            Runs a specified command for each file in a set of files.
    FORMAT         Formats a disk for use with Windows.
    FSUTIL         Displays or configures the file system properties.
    FTYPE          Displays or modifies file types used in file extension associations.
    GOTO           Directs the Windows command interpreter to a labeled line in a batch program.
    GPRESULT       Displays Group Policy information for machine or user.
    HELP           Provides Help information for Windows commands.
    ICACLS         Display, modify, backup, or restore ACLs for files and directories.
    IF             Performs conditional processing in batch programs.
    LABEL          Creates, changes, or deletes the volume label of a disk.
    MD             Creates a directory.
    MKDIR          Creates a directory.
    MKLINK         Creates Symbolic Links and Hard Links
    MODE           Configures a system device.
    MORE           Displays output one screen at a time.
    MOVE           Moves one or more files from one directory to another directory.
    OPENFILES      Displays files opened by remote users for a file share.
    PATH           Displays or sets a search path for executable files.
    PAUSE          Suspends processing of a batch file and displays a message.
    POPD           Restores the previous value of the current directory saved by PUSHD.
    PRINT          Prints a text file.
    PROMPT         Changes the Windows command prompt.
    PUSHD          Saves the current directory then changes it.
    RD             Removes a directory.
    RECOVER        Recovers readable information from a bad or defective disk.
    REM            Records comments (remarks) in batch files or CONFIG.SYS.
    REN            Renames a file or files.
    RENAME         Renames a file or files.
    REPLACE        Replaces files.
    RMDIR          Removes a directory.
    ROBOCOPY       Advanced utility to copy files and directory trees
    SET            Displays, sets, or removes Windows environment variables.
    SETLOCAL       Begins localization of environment changes in a batch file.
    SC             Displays or configures services (background processes).
    SCHTASKS       Schedules commands and programs to run on a computer.
    SHIFT          Shifts the position of replaceable parameters in batch files.
    SHUTDOWN       Allows proper local or remote shutdown of machine.
    SORT           Sorts input.
    START          Starts a separate window to run a specified program or command.
    SUBST          Associates a path with a drive letter.
    SYSTEMINFO     Displays machine specific properties and configuration.
    TASKLIST       Displays all currently running tasks including services.
    TASKKILL       Kill or stop a running process or application.
    TIME           Displays or sets the system time.
    TITLE          Sets the window title for a CMD.EXE session.
    TREE           Graphically displays the directory structure of a drive or path.
    TYPE           Displays the contents of a text file.
    VER            Displays the Windows version.
    VERIFY         Tells Windows whether to verify that your files are written correctly to a disk.
    VOL            Displays a disk volume label and serial number.
    XCOPY          Copies files and directory trees.
    WMIC           Displays WMI information inside interactive command shell.""".split("\n")
    for i in x:
        addq(f"What function {i[15].lower()}{i[16:].strip().strip(".")}?", i[:15].strip().capitalize())

if what == 2 or what == 3:

    addq("What is a useful workshop for pressing liquids from various sources?", "Screw Press")
    addq("Where do you use tallow (rendered fat) or oil here with lye to make soap where some plants might need to be milled first before they can be used and empty jugs are required to store the liquid products.", "Soap Maker's Workshop")
    addq("What is a short, sturdy creature fond of drink and industry?", "Dwarf")
    addq("What is a squat amphibian with leathery skin, found in relatively dry areas?", "Toad")
    addq("What is a dark green man with the distinct head of a toad?", "Toad Man")
    addq("What is a huge monster in the shape of a toad?", "Giant Toad")
    addq("What is a worm-like creature with the torso of a man?", "worm man")
    addq("What is a tiny burrowing creature, found in moist soil which is legless, long and thin?", "worm")
    addq("What is a huge bird monster with extremely long legs and neck?", "ostrich giant")
    addq("What is tis is a medium-sized creature with legs and arms, but the long neck and head of an ostrich?", "ostrich man")
    addq("What is a large flightless bird that runs through the savanna which has a long neck and legs?", "ostrich")
    addq("What is a large monster with a long nose and brown feathers?", "kiwi giant")
    addq("What is a person with the head and feathers of a kiwi?", "kiwi man")
    addq("What is a small, brown, flightless bird which eats insects and grubs and is known for its keen sense of smell?", "kiwi")      
    addq("What is a large bird monster that is the same shape as a peregrine falcon?", "giant peregrine falcon")
    addq("What is a person with the head and wings of a peregrine falcon?", "peregrine falcon man")
    addq("What is a small bird of prey that is capable of great speed which dive on unsuspecting vermin?", "falcon peregrine")        
    addq("What is a huge monster, shaped like a penguin?", "penguin giant")
    addq("What is a humanoid with the head, feet, and feathers of a penguin?", "penguin man")
    addq("What is a small flightless bird, it is the largest of the natural penguins which is known for its treks through leagues of glacial ice?", "penguin emperor")
    addq("What is a small flightless bird, blue in color, that lives on arctic shorelines?", "little penguin")
    addq("What is a small flightless bird that lives on arctic shorelines?", "penguin")
    addq("What is a huge monster in the form of a red-winged blackbird?", "giant red-winged blackbird")
    addq("What is a person with the head and wings of a red-winged blackbird?", "red-winged blackbird man")
    addq("What is a small black bird with bright red markings under the wings which live in the marshland?", "red-winged blackbird")
    addq("What is a huge monster in the form of an oriole?", "giant oriole")
    addq("What is a person with the head and wings of an oriole?", "oriole man")
    addq("What is a small yellow and black bird which feed in the canopy of the forest?", "oriole")
    addq("What is a huge monster in the form of a grackle?", "giant grackle")
    addq("What is a person with the head and wings of a grackle?", "grackle man")
    addq("What is a small gregarious bird, blue and black with yellow eyes, found in temperate pastures?", "grackle")
    addq("What is a huge monster in the form of a cardinal?", "giant cardinal")
    addq("What is a person with the head and wings of a cardinal?", "cardinal man")
    addq("What is a small bright red bird with a distinctive crest, found in temperate forests?", "cardinal")
    addq("What is a huge monster in the form of a bluejay?", "giant bluejay")
    addq("What is a person with the head and wings of a bluejay?", "bluejay man")
    addq("What is a small blue-crested bird living in temperate woodlands, known for its harsh chirps?", "bluejay")

    addq("What is a huge monster in the form of a bushtit?", "giant bushtit")
    addq("What is a person with the head and wings of a bushtit?", "bushtit man")
    addq("What is a tiny brown bird found in open woodlands?", "bushtit")
    addq("What is a huge monster in the form of a masked lovebird?", "giant masked lovebird")
    addq("What is a colorful person with the head and wings of a masked lovebird?", "masked lovebird man")
    addq("What is a tiny, colorful bird which can be trained to be a pleasant companion?", "masked lovebird")
    addq("What is a huge monster in the shape of a hornbill?", "giant hornbill")
    addq("What is a feathered person with a brightly-colored bill?", "hornbill man")
    addq("What is a tiny bird with a large, brightly-colored bill?", "hornbill")
    addq("What is a huge monster in the form of an eagle?", "giant eagle")
    addq("What is a feathered person with the head and wings of an eagle?", "eagle man")
    addq("What is a small bird of prey?", "eagle")
    addq("What is a huge monster in the shape of a great horned owl?", "giant great horned owl")
    addq("What is a feathered person with the head and wings of a great horned owl?", "great horned owl man")
    addq("What is a small, nocturnal bird of prey with large eyes and protruding feathers?", "great horned owl")
    addq("What is a huge monster in the shape of an albatross?", "giant albatross")
    addq("What is a person with the head and wings of an albatross?", "albatross man")
    addq("What is a small sea bird with great wings which soars through the sky and dives for food on the surface of the water?", "albatross")
    addq("What is a huge monster in the shape of a kestrel?", "giant kestrel")
    addq("What is a person with the head and wings of a kestrel?", "kestrel man")
    addq("What is a tiny bird of prey which hovers above the ground and swoops down to snatch rodents and mice?", "kestrel")
    addq("What is a huge monster in the shape of a magpie?", "giant magpie")
    addq("What is a person with the head and wings of a magpie?", "magpie man")
    addq("What is a tiny black and white bird which is one of the most intelligent of the natural creatures?", "magpie")
    addq("What is a huge monster taking the shape of a peach-faced lovebird?", "giant peach-faced lovebird")
    addq("What is a colorful person with the head and wings of a peach-faced lovebird?", "peach-faced lovebird man")
    addq("What is a tiny, brightly colored parrot which are clever and learn many tricks?", "peach-faced lovebird")
    addq("What is a large monster in the form of a cockatiel?", "giant cockatiel")
    addq("What is a crested person with the head and wings of a cockatiel?", "cockatiel man")
    addq("What is a tiny crested parrot which are prized as domestic companions?", "cockatiel")
    addq("What is a huge monster in the form of an emu?", "giant emu")
    addq("What is a feathered person with the head of an emu?", "emu man")
    addq("What is a large flightless bird which is very curious and has been known to follow other creatures?", "emu")
    addq("What is a large monster in the form of an osprey?", "giant osprey")
    addq("What is a person with the head and wings of an osprey?", "osprey man")
    addq("What is a small bird of prey with black markings on its eyes which hunts near bodies of water?", "osprey")
    addq("What is a huge monster in the form of a wren?", "giant wren")
    addq("What is a person with the head and wings of a wren?", "wren man")
    addq("What is a tiny brown bird given to singing complex songs?", "wren")
    addq("What is a large monster in the shape of a lorikeet?", "giant lorikeet")
    addq("What is a colorful person with the head and wings of a lorikeet?", "lorikeet man")
    addq("What is a tiny, brightly-colored tree parrot which uses its tongue to feed on plants?", "lorikeet")
    addq("What is a large monster in the form of a swan?", "giant swan")
    addq("What is a person with the head and wings of a swan?", "swan man")
    addq("What is a small aquatic bird, prized I for its beauty?", "swan")
    addq("What is a large monster in the form of a puffin?", "giant puffin")
    addq("What is a feathered person with the head of a puffin?", "puffin man")
    addq("What is a tiny diving bird found living on seaside cliffs in the colder climates?", "puffin")
    addq("What is a huge monster in the shape of a grey parrot?", "giant grey parrot")
    addq("What is a person with the head and wings of a grey parrot?", "grey parrot man")
    addq("What is te most intelligent of birds which can be found in the rainforest?", "grey parrot")
    addq("What is a large monster the shape of a kakapo?", "giant kakapo")
    addq("What is a person with the head and wings of a kakapo?", "kakapo man")
    addq("What is a small flightless green parrot which is nocturnal and counts itself among the longest-lived birds?", "kakapo")
    addq("What is a large monster in the shape of a parakeet?", "giant parakeet")
    addq("What is a person with the head and wings of a parakeet?", "parakeet man")
    addq("What is a tiny parrot found in flocks of many hundreds with exceptional birds that can be taught to speak?", "parakeet")
    addq("What is a large monster in the form of a barn owl?", "giant barn owl")
    addq("What is a person with the arms and wings of a barn owl?", "barn owl man")
    addq("What is a small, nocturnal bird of prey found in woodland regions which's hunger for rodents drives it to take residence in buildings?", "barn owl")
    addq("What is a large monster in the shape of a loon?", "giant loon")
    addq("What is a person with the head and wings of a loon?", "loon man")
    addq("What is a small water bird found in remote lakes which is known for its haunting call?", "loon")
    addq("What is a large monster in the form of a stork?", "giant white stork")
    addq("What is a person with the head and wings of a stork, also standing on long legs?", "white stork man")
    addq("What is a small bird with long legs and bill, and a extremely long wingspan?", "white stork")
    addq("What is a large bird-like monster in the shape of a sparrow?", "giant sparrow")
    addq("What is a person with the head and wings of a sparrow?", "sparrow man")
    addq("What is a tiny brown bird that can be found in most temperate regions?", "sparrow")
    addq("What is a large bird monster in the shape of a snowy owl?", "giant snowy owl")
    addq("What is a person with the wings and head of a snowy owl?", "snowy owl man")
    addq("What is a small white bird that hunts in the coldest reaches of the world?", "snowy owl")
    addq("What is a monster many times the size of an ordinary kea?", "giant kea")
    addq("What is a green person with the head of a kea?", "kea man")
    addq("What is a small, green, intelligent mountain parrot?", "kea")
    addq("What is a huge monster in the shape of a cassowary?", "giant cassowary")
    addq("What is a brightly-colored person with the head of a cassowary?", "cassowary man")
    addq("What is a small, flightless, brightly-colored bird?", "cassowary")
    addq("What is a large bird-like monster, even more deadly when found in groups?", "giant raven")
    addq("What is a person with the head and wings of a raven?", "raven man")
    addq("What is a small, foreboding black bird that feeds on carrion which is social, very intelligent, and knows how to use tools?", "raven")
    addq("What is a large bird-like monster, even more deadly when found in groups?", "giant crow")
    addq("What is a small person with the head and wings of a crow?", "crow man")
    addq("What is a small black bird that feeds on carrion which is social, very intelligent and knows how to use tools?", "crow")

    addq("What is a huge monster in the form of a snail?", "giant snail")
    addq("What is a creature with the shape of a man, but with stalks for eyes, and a great shell on its back?", "snail man")
    addq("What is a tiny land mollusk with a large shell?", "snail")
    addq("What is a huge monster in the shape of a brown recluse spider?", "giant brown recluse spider")
    addq("What is a person with the head and arms of a brown recluse spider?", "brown recluse spider man")
    addq("What is a tiny brown bug known for its powerful poison?", "brown recluse spider")
    addq("What is a huge monster in the shape of a moon snail?", "giant moon snail")
    addq("What is a colorful person with the head and shell of a moon snail?", "moon snail man")
    addq("What is a tiny predatory mollusk which is brightly colored?", "moon snail")
    addq("What is a tiny insect capable of destroying large wooden structures when in large numbers?", "mite")
    addq("What is a huge monster in the form of a jumping spider?", "giant jumping spider")
    addq("What is a person with the head and arms of a jumping spider?", "jumping spider man")
    addq("What is a tiny black bug that lacks a web but can leap short distances?", "jumping spider")
    addq("What is a huge monster in the shape of a mosquito?", "giant mosquito")
    addq("What is a person with the head and wings of a mosquito?", "mosquito man")
    addq("What is a tiny pest insect which uses its long nose to suck blood from its host?", "mosquito")
    addq("What is a huge monster in the form of a slug?", "giant slug")
    addq("What is a great slug with the torso of a man which pulls itself across the ground with its hands for greater speed?", "slug man")  
    addq("What is a tiny land mollusk which can be found under rotten logs and in gardens?", "slug")
    addq("What is a huge monster in the form of a thrips?", "giant thrips")
    addq("What is a person with the head and wings of a thrips?", "thrips man")
    addq("What is a tiny pest insect which feeds on both crops and other bugs?", "thrips")
    addq("What is a huge monster in the shape of a louse?", "giant louse")
    addq("What is a person with the head and legs of a louse?", "louse man")
    addq("What is a tiny parasitic insect which feeds on skin and blood?", "louse")
    addq("What is a large monster taking the shape of a tick?", "giant tick")
    addq("What is a person with the head and legs of a tick?", "tick man")
    addq("What is a tiny, blood-sucking bug found in wooded areas?", "tick")
    addq("What is a large monster in the shape of a mantis?", "giant mantis")
    addq("What is a green person with the head and arms of a mantis?", "mantis man")
    addq("What is a tiny green insect which has long, distinctive forelimbs that it uses to catch its prey?", "mantis")
    addq("What is a huge monster in the form of a bark scorpion?", "giant bark scorpion")
    addq("What is a person with the head, pincers and tail of a bark scorpion?", "bark scorpion man")
    addq("What is a tiny yellow bug which has pincers and a stinging tail which can prove fatal?", "bark scorpion")
    addq("What is a huge creature in the shape of a grasshopper?", "giant grasshopper")
    addq("What is a person with the head and legs of a grasshopper?", "grasshopper man")
    addq("What is a tiny insect which uses its powerful legs to leap and make noise?", "grasshopper")
    addq("What is a large monster in the form of a moth?", "giant moth")
    addq("What is a person with the head and wings of a moth?", "moth man")
    addq("What is a tiny nocturnal insect which flies toward flames in the night?", "moth")
    addq("What is a large monster in the shape of a damselfly?", "giant damselfly")
    addq("What is a person with the wings and head of a damselfly?", "damselfly man")
    addq("What is a tiny, colorful, long-bodied insect?", "damselfly")

    addq("What is a huge beast in the form of a gila monster?", "giant gila monster")
    addq("What is a venomous person with the head and tail of a gila monster?", "gila monster man")
    addq("What is a small venomous lizard?", "gila monster")
    addq("What is a large monster in the form of a desert tortoise?", "giant desert tortoise")
    addq("What is a reptile person with the head and tail of a desert tortoise?", "desert tortoise man")
    addq("What is a tiny shelled reptile that lives in the desert?", "desert tortoise")
    addq("What is a large monster in the shape of a gecko?", "giant leopard gecko")
    addq("What is a person with the head and fingers of a gecko?", "leopard gecko man")
    addq("What is a tiny, brightly-colored lizard?", "leopard gecko")

    addq("What is a small lagomorph with long ears which has powerful hind legs which it uses to swiftly avoid predators which can be found anywhere from forests to deserts?", "rabbit")
    addq("What is a small forest bird known for the distinctive flaps of skin hanging from its face which is prized for its meat?", "turkey")
    addq("What is a small forest bird which the male's tail creates an extravagant display for females which at night, they roost in the trees?", "blue peafowl")
    addq("What is a small ground-dwelling bird which has a featherless head and eats seeds and insects which moves about in groups?", "guineafowl")
    addq("What is a large domestic animal with a long neck which has been bred for its valuable hair?", "alpaca")
    addq("What is a large domestic pack animal which has a long neck which is prized for its hair?", "llama")
    addq("What is a large mammalian herbivore which has long fur and curving horns which can be found in the mountains?", "yak")
    addq("What is a small migratory bird which has a very long neck and can be found in lakes and other bodies of water?", "goose")     
    addq("What is a large mammalian herbivore living in cold climates which has large antlers and sought-after fur?", "reindeer")
    addq("What is a large mammalian herbivore which is powerfully built and has long curved horns?", "water buffalo")
    addq("What is a small water bird which has a long neck and powerful legs meant for swimming and diving?", "duck")
    addq("What is a small rodent with no tail which can be found roaming the grassland in herds which has three toes on its hind feet?", "cavy")
    addq("What is a small domestic bird capable of flying short distances which is prized for its tasty eggs?", "chicken")
    addq("What is a medium-sized herding animal which is known for its short horns and beard?", "goat")
    addq("What is a medium-sized domestic animal which has a distinctive snout and corkscrew tail which is thought by some to be intelligent?", "pig")
    addq("What is a medium-sized herding animal which is prized for its thick wool coat?", "sheep")
    addq("What is a large mammalian herbivore which often bear large horns and the males are ill-tempered which are domesticated for milk and meat?", "cow")
    addq("What is a large hooved, maned herbivore which can run swiftly and many are domesticated as steeds?", "horse")
    addq("What is a medium-sized, hooved herbivore which are domesticated as beasts of burden?", "donkey")
    addq("What is a compact offspring of horse and donkey, bred to be a beast of burden?", "mule")
    addq("What is a small mammalian carnivore which is usually domestic and hunts vermin?", "cat")
    addq("What is a medium-sized highly social mammalian carnivore which has a keen sense of smell which can be trained to obey commands?", "dog")

    addq("What is a rolling platform for carrying passengers or cargo?", "wagon")
    addq("What is a small woolly insect that lives in hive colonies which has an annoying sting which it rarely uses?", "bumblebee")
    addq("What is a small flying insect that lives in large colonies which has a powerful stinger on its tail which's hives are prized for their honey?", "honey bee")
    addq("What is a large monster in the shape of a dragonfly?", "giant dragonfly")
    addq("What is a person with the wings and head of a dragonfly?", "dragonfly man")
    addq("What is a relatively large insect found in swamps and marshland?", "dragonfly")
    addq("What is a large monster in the shape of a firefly?", "giant firefly")
    addq("What is a person with the wings and head of a firefly?", "firefly man")
    addq("What is a tiny flying insect that can be seen at night by its glowing tail?", "firefly")
    addq("What is a large monster in the shape of a monarch butterfly?", "giant butterfly monarch")
    addq("What is a person with the wings and head of a monarch butterfly?", "butterfly monarch man")
    addq("What is a small insect with large orange wings which is admired for its beauty?", "butterfly monarch")
    addq("What is tis tiny insect can be found in huge colonies in the dirt which overwhelm their enemies with swarms which have poison bites?", "ant")
    addq("What is a large monster in the shape of a beetle?", "giant beetle")
    addq("What is a person with the carapace and head of a beetle?", "beetle man")
    addq("What is a tiny insect that can be found almost anywhere outside?", "beetle")
    addq("What is a large monster in the shape of a roach?", "giant roach")
    addq("What is a person with the wings and head of a roach?", "roach man")
    addq("What is a small insect that seeks out unwatched food and garbage which fear light?", "large roach")
    addq("What is a large monster in the shape of a fly?", "giant fly")
    addq("What is a person with the wings and head of a fly?", "fly man")
    addq("What is a tiny flying insect found around rotting meat and garbage which are widely considered to be a nuisance?", "fly")

    addq("What is a tiny, foul-tempered humanoid creature that dwells in the evil mountains which are known to enjoy drinking liquor and will take any unguarded supplies of booze?", "dark gnome")
    addq("What is a tiny, jolly humanoid creature that dwells in the fair mountains which are known to enjoy drinking liquor and don't care whether it's theirs or not?", "mountain gnome")
    addq("What is a large creature the shape of a hoary marmot?", "giant hoary marmot")
    addq("What is a person with the head and fur of a hoary marmot?", "hoary marmot man")
    addq("What is a large rodent that lives in groups in the high mountains?", "hoary marmot")
    addq("What is a huge monster in the form of a mountain goat?", "giant mountain goat")
    addq("What is a horned person with the head of a mountain goat?", "mountain goat man")
    addq("What is a medium-sized herbivore that lives in the high mountains, able to navigate the slopes despite its hooved feet?", "mountain goat")

    addq("What is a huge sea monster with an enormous horn on its nose?", "giant narwhal")
    addq("What is a medium-sized creature with the arms and torso on a man, but with the head and tail of a narwhal?", "narwhal man")       
    addq("What is a medium-sized sea mammal with a long thin horn on its nose which uses this horn to communicate and break up ice?", "narwhal")
    addq("What is a large oceanic fish capable of great speed?", "bluefin tuna")
    addq("What is a large, long fish with many sharp fangs which hunts by ambushing its prey?", "great baracuda")
    addq("What is a large, flat, oceanic fish which dwells on the sea floor, both its eyes on the top side?", "halibut")
    addq("What is a huge oceanic fish capable of great speed which has a long, sharp snout used for slashing its prey?", "marlin")      
    addq("What is a huge predatory fish found in open ocean which has a long pointed bill which it uses to slash and ram?", "swordfish")
    addq("What is a giant oceanic creature resembling a huge fish's head connected to a wide tail?", "ocean sunfish")
    addq("What is a medium-sized oceanic fish which is fork-tailed and sought after for its meat?", "bluefish")
    addq("What is a large, big-mouthed fish, found around coral reefs?", "giant grouper")
    addq("What is a large oceanic fish which is flat, round and red?", "opah")
    addq("What is a medium-sized oceanic fish, often hunted for its meat?", "cod")
    addq("What is a medium-sized fish found around coasts and islands which is easy prey for predators?", "milkfish")
    addq("What is a medium-sized, brown, snake-like fish found in ocean waters?", "eel conger")
    addq("What is a large oceanic fish covered with bony plates?", "sturgeon")
    addq("What is an elusive medium-sized fish found in coastal waters?", "coelacanth")
    addq("What is a medium-sized, flat fish which lives near the beach and will defend itself with sharp barbs?", "stingray")
    addq("What is a huge filter-feeding fish with great wings which travel the oceans and are curious and friendly?", "manta ray")    
    addq("What is a medium-sized, flat, bottom-dwelling fish?", "common skate")
    addq("What is a large, flat, camouflaged fish found on the sea floor in temperate waters which is quite passive?", "angel shark")        
    addq("What is a large, dangerous fish, often found hunting solitarily along coastlines?", "hammerhead shark")
    addq("What is a large, dangerous fish found hunting in packs in any ocean?", "blue shark")
    addq("What is a medium-sized fish which shelters in caves on the shallow sea floor which hunts for food in packs but is not aggressive?", "whitetip reef shark")
    addq("What is a medium-sized fish found in shallow oceanic waters?", " blacktip reef shark")
    addq("What is a medium-sized, aggressive, territorial fish which can be found in shallow oceanic waters, and has also been known to travel up large rivers?", "bull shark")
    addq("What is a giant, striped, oceanic fish known to devour anything in its path?", "tiger shark")
    addq("What is a large fish which scavenges along tropical and temperate coastal waters?", "longfin mako shark")
    addq("What is a large, aggressive, oceanic fish with a mouth full of pointed teeth which is capable of great speed?", "shortfin mako shark")
    addq("What is a large nocturnal bottom-dwelling fish which is sluggish in movement and found in near-tropical shores?", "nurse shark")   
    addq("What is a gigantic filter-feeding fish found in temperate oceans?", "basking shark")
    addq("What is a gigantic filter-feeding fish found in tropical oceans?", "whale shark")
    addq("What is a huge fish covered with growths and spots it uses to hide on the sea bed which is not usually aggressive?", "spotted wobbegong shark")
    addq("What is a large fish found in coastal temperate waters?", "dogfish spiny shark")
    addq("What is a large eel-like fish found in coastal waters?", "frill shark")
    addq("What is a giant oceanic fish with rows and rows of razor-sharp pointed teeth?", "white great shark")
    addq("What is a small oceanic eel-like creature that latches onto the side of its victim and tears into them?", "sea lamprey")     
    addq("What is a giant monster in the form of a walrus?", "giant walrus")
    addq("What is a legless person with the head and back flippers of a walrus?", "walrus man")
    addq("What is a huge aquatic mammal with giant tusks and dense whiskers which are thick and blubbery and live almost exclusively on mussels?", "walrus")

    addq("What is a huge monster, the shape of a platypus?", "giant platypus")
    addq("What is a humanoid with the head, tail and poison spurs of a platypus?", "platypus man")
    addq("What is a small semi-aquatic, egg laying mammal with a bill, flat tail and poison spurs?", "platypus")
    addq("What is a medium-sized, green fish found in temperate lakes?", "pike")
    addq("What is a medium-sized predatory fish found in lakes and streams which is known for its ferocious attacks and interlocking teeth?", "tigerfish")
    addq("What is a medium-sized fish found in lakes and streams which are bottom-feeders and tend to gather in groups?", "carp")
    addq("What is a medium-sized fish with a long snout which is found in lakes and streams?", "longnose gar")
    addq("What is a huge hippo-shaped monster?", "giant hippo")
    addq("What is a large person with the head of a hippo?", "hippo man")
    addq("What is a huge, round, hairless river creature which is a plant-eating animal but has long tusks and can be aggressive and deadly if disturbed?", "hippo")

    addq("What is a large monster with the shape of a red panda?", "giant panda")
    addq("What is a medium-sized, walking red panda with arms and a tail which prefers the forest and its beloved trees?", "panda man")     
    addq("What is a small tree-dwelling mammal with distinctive color which rears up on its hind legs when cornered which uses its front paws like hands?", "panda")
    addq("What is a huge monster the shape of a moose?", "giant moose")
    addq("What is a humanoid with the head and antlers of a moose?", "moose man")
    addq("What is a large mammal with great antlers and a large nose. It lives in temperate forests?", "moose")
    addq("What is a huge monster the shape of a badger which is ferocious in combat?", "giant badger")
    addq("What is a humanoid with the head and stripes of a badger?", "badger man")
    addq("What is a small mammal with a striped face which lives in groups and is ferocious in combat?", "badger")
    addq("What is a humanoid with the head of a capybara which is fond of swimming?", "capybara man")
    addq("What is a huge rodent that walks on tall legs which's bark can be heard at large distances which is fond of swimming?", "giant capybara")
    addq("What is a medium-sized semi-aquatic rodent which lives in large herds and barks when alarmed?", "capybara")
    addq("What is a humanoid creature with the head and belly of a panda?", "panda man")
    addq("What is a giant bear-like creature found in the wildest parts of the world which has striking black and white fur?", "gigantic panda")
    addq("What is a large bear-like creature with a striking coat of black and white hair which feeds on bamboo forests?", "panda")
    addq("What is a huge monster in the form of a buzzard?", "giant buzzard")
    addq("What is a person with the head and wings of a buzzard?", "buzzard man")
    addq("What is a medium-sized, red-faced black bird that searches the temperate lands for carrion?", "buzzard")
    addq("What is a huge monster in the shape of an alligator?", "giant alligator")
    addq("What is a person with the head and tail of an alligator?", "alligator man")
    addq("What is a huge reptile, found in rivers and marshlands which is an ambush predator, solitary and territorial?", "alligator")        
    addq("What is a large creature the shape of a groundhog?", "giant groundhog")
    addq("What is a person with the head and fur of a groundhog?", "groundhog man")
    addq("What is a large, round, lowland rodent which lives in burrows in the ground and ventures out to eat?", "groundhog")
    addq("What is a huge monster in the shape of a wolf?", "giant wolf")
    addq("What is a person with the head and tail of a wolf?", "wolf man")
    addq("What is a large canine found in temperate regions which is territorial and hunts in packs?", "wolf")
    addq("What is a huge monster in the form of a cougar?", "giant cougar")
    addq("What is a person with the head and tail of a cougar?", "cougar man")
    addq("What is a large solitary feline which is found most often in dense vegetation, ambushing its prey?", "cougar")
    addq("What is a large monster in the form of a rhesus macaque?", "giant rhesus macaque")
    addq("What is a person with the head and tail of a rhesus macaque?", "rhesus macaque man")
    addq("What is a medium-sized monkey found in woods and grassland which usually lives on roots and insects but can become a pest in civilized areas, roaming in large groups and begging for scraps?", "rhesus macaque")
    addq("What is a huge monster in the shape of a raccoon?", "giant raccoon")
    addq("What is a person with the mask and tail of a raccoon?", "racoon man")
    addq("What is a small omnivorous animal with a bright mask of fur which is nocturnal and found in temperate forests which is a curious animal and has been known to steal from civilized areas?", "racoon")
    addq("What is a huge monster in the shape of a fox?", "giant fox")
    addq("What is a person with the head and tail of a fox?", "fox man")
    addq("What is a small carnivorous animal found in temperate climatesv has orange fur and is known for its cleverness?", "fox")       
    addq("What is a huge monster in the form of a deer?", "giant deer")
    addq("What is a person with the head of a deer?", "deer man")
    addq("What is a medium-sized hoofed forest creature that grows its antlers back each year?", "deer")
    addq("What is a huge monster in the shape of a black bear?", "giant black bear")
    addq("What is a large person with the head of a black bear?", "bear black bear")
    addq("What is a large omnivorous predator found in temperate woodlands which is mainly living on berries, it will also steal carcasses from other hunters which is though normally a docile animal, it has been known to kill in a predatory attack?", "black bear")
    addq("What is a huge monster in the shape of a grizzly bear?", "giant grizzly bear")
    addq("What is a large person with the head of a grizzly bear?", "grizzly bear man")
    addq("What is a huge brown creature found in temperate woodland which is known for its ferocious attack, usually when it or its young are threatened?", "grizzly bear")

    addq("What is a large monster the shape of an armadillo which has thick armor for skin?", "giant armadillo")
    addq("What is a person with the hide and head of an armadillo?", "armadillo man")
    addq("What is a small mammal with a leathery hide which can roll into a ball to escape predators?", "armadillo")
    addq("What is a huge monster with an enormous shell?", "gigantic tortoise")
    addq("What is a person with a large shell and the head of a giant tortoise?", "giant tortoise man")
    addq("What is a medium-sized reptile with a large shell which can retreat into its shell to escape predators?", "giant tortoise")        
    addq("What is a huge monster the shape of a honey badger which is ferocious in combat?", "giant honey badger")
    addq("What is a humanoid with the head and stripes of a honey badger?", "honey badger man")
    addq("What is a small mammal known to defend itself ferociously in combat, often fighting off multiple animals many times its size?", "honey badger")
    addq("What is a huge monster the shape of a giraffe?", "giant giraffe")
    addq("What is a person with the head and neck of a giraffe?", "giraffe man")
    addq("What is a huge leaf-eating mammal which has an extremely long neck which's skin has a distinctive brown and white pattern?", "giraffe")
    addq("What is a huge monster the shape of a rhinoceros?", "giant rhinoceros")
    addq("What is a person with the head and horns of a rhinoceros?", "rhinoceros man")
    addq("What is a huge herbivore with thick plated skin and powerful build which is known for the thick horns on the end of its nose?", "rhinoceros")
    addq("What is a huge monster in the form of a vulture?", "giant vulture")
    addq("What is a person with the head and wings of a vulture?", "vulture man")
    addq("What is a large bird with a featherless red head found in the sky of tropical deserts, scanning the ground for dead carcasses?", "vulture")
    addq("What is a huge monster in the shape of a saltwater crocodile?", "giant saltwater crocodile")
    addq("What is a person with the head and tail of a saltwater crocodile?", "saltwater crocodile man")
    addq("What is a huge, predatory reptile found in coastal marshes and river deltas which ambushes its prey at the shore and uses its great size to drag the victim under and drown them?", "saltwater crocodile")
    addq("What is a huge monster the shape of a two-humped camel?", "giant two-humped camel")
    addq("What is a person with the head and humps of a two-humped camel?", "two-humped camel man")
    addq("What is a large, long-necked creature with two fleshy humps on its back which is domesticated to carry passengers and cargo?", "two-humped camel")
    addq("What is a huge monster the shape of a one-humped camel?", "giant one-humped camel")
    addq("What is a person with the head and hump of a one-humped camel?", "one-humped camel man")
    addq("What is a large long-necked creature with a large hump on its sturdy body which has been domesticated to carry passengers and cargo but is nonetheless bad-tempered and will spit?", "one-humped camel")
    addq("What is a small ape from the tropical forest which can be found in the trees eating fruit?", "black crested gibbon")
    addq("What is a small fruit-eating ape, found in the trees?", "white browed gibbon")
    addq("What is a small ape that swings from the trees, eating fruit?", "bilou gibbon")
    addq("What is a small ape found in pairs, swinging from the trees?", "pileated gibbon")
    addq("What is a small ape found in the trees eating fruit?", "silvery gibbon")
    addq("What is a small ape found in the trees of the tropical forest which is known for its calls?", "gray gibbon")
    addq("What is a small fruit-eating ape, found in the trees?", "black handed gibbon")
    addq("What is a small, long-armed ape which lives in trees and eats fruit?", "white handed gibbon")
    addq("What is a medium-sized ape found in the trees which is known for its loud calls?", "siamang gibbon")
    addq("What is a huge intelligent ape found in the tropical forests which is bright red and found living in the trees?", "orangutan")     
    addq("What is a huge ape found in the forest which lives in small groups eating plants with the groups being lead by a large dominant male with a silver back?", "gorilla")
    addq("What is a large ape which lives in the tropical forests which is quite intelligent and lives in large and complex social groups?", "bonobo")
    addq("What is a large ape which lives in the tropical forests which lives in complex social groups of many members which though is quite intelligent, it has been known for ferocious attacks?", "himpanzee")
    addq("What is a large monster in the form of a mandrill?", "giant mandrill")
    addq("What is a blue-rumped person with the head and tail of a mandrill?", "mandrill man")
    addq("What is a large monkey with blue face and rump which lives in large groups and often survives by destroying crops and stealing garbage which the males being larger, with powerful jaws?", "mandrill")
    addq("What is a huge monster in the form of a gazelle?", "giant gazelle")
    addq("What is a horned person with the head of a gazelle?", "gazelle man")
    addq("What is a small hooved creature found in large groups in the grasslands which has short horns and moves by leaps and bounds?", "gazelle")
    addq("What is a gigantic spotted cat which is possibly the fastest animal on land and is found in the savage wilds?", "giant cheetah")   
    addq("What is a spotted person with the head and tail of a cheetah?", "heetah man")
    addq("What is a large spotted feline predator which is capable of incredible speed when ambushing its prey?", "heetah")
    addq("What is te largest of the giant cats which can be found hunting alone in the most savage countryside?", "giant tiger")
    addq("What is an orange striped person with the head of a tiger?", "iger man")
    addq("What is a huge, striped predator which is found in almost any climate on a lone hunt for its prey?", "iger")
    addq("What is a gigantic feline predator, similar to its cousins in all but size which can be found in the savage wilderness?", "giant jaguar")
    addq("What is a spotted person with the head and tail of a jaguar?", "jaguar man")
    addq("What is a large, muscular, spotted feline found in tropical jungles which is solitary and stalks and ambushes its prey?", "jaguar")
    addq("What is a gigantic spotted predator, dwarfing its small cousins which is found in the wild lands?", "giant leopard")
    addq("What is a spotted person with the head and tail of a leopard?", "leopard man")
    addq("What is a large spotted feline found in grass and woodland which is known for great speed in hunting?", "leopard")
    addq("What is a gigantic version of the feline predator which's giant prides can be found in the wildest, most savage parts of the world?", "giant lion")
    addq("What is a person with the head of a lion?", "lion man")
    addq("What is a large ferocious predator found in grasslands which lives in groups of females and one male with a large mane which hunt together and are capable of felling extremely large prey?", "lion")
    addq("What is a huge monster warthog with jagged tusks?", "giant warthog")
    addq("What is a person with the head of a warthog?", "warthog man")
    addq("What is a medium-sized animal living in grass and woodland which has a large snout with four sharp tusks which will aggressively defend itself?", "warthog")
    addq("What is a gigantic monster in elephant form?", "giant elephant")
    addq("What is a large person with the trunk and ears of an elephant?", "lephant man")
    addq("What is a huge, hairless mammal, found grazing in grasslands in groups which eats plants which it lifts up with its long trunk which when angered, will attack with its long tusks?", "lephant")

    addq("What is a huge monster in the shape of a polar bear?", "giant polar bear")
    addq("What is a large person with the head of a polar bear?", "polar bear man")
    addq("What is a huge predatory mammal covered in white hair which hunts the shores along tundra and glaciers?", "polar bear")
    addq("What is a huge monster in the form of an elk?", "giant elk")
    addq("What is a person with the head of an elk?", "elk man")
    addq("What is a large hooved animal found roaming wild in temperate forests which males have long antlers?", "elk")
    addq("What is a huge monster in the form of a muskox?", "giant muskox")
    addq("What is a horned person with the head of a muskox?", "muskox man")
    addq("What is a large hooved animal with curved horns and a thick brown coat which is known for its strong odor?", "muskox")

    addq("What is a large monster in the shape of a chinchilla?", "giant chinchilla")
    addq("What is a hairy person with the head and tail of a chinchilla?", "chinchilla man")
    addq("What is a tiny furry rodent dwelling in the hollow cracks of rocks which can be found high in the mountains?", "chinchilla")      
    addq("What is a large, terrifying monster the shape of a wolverine?", "giant wolverine")
    addq("What is a person with the head and tail of a wolverine?", "wolverine man")
    addq("What is a small, muscular, weasel-like creature which is known for its ferocity?", "wolverine")

    addq("What is a strange crystalline creature the shape of a man which is found deep underground?", "elementman amethyst")
    addq("What is a strange shapeless life form with an orange leathery skin containing a liquid interior which can secrete its internal fluid?", "cave blob")
    addq("What is a small humanoid resembling a walking mushroom with arms and legs which lives far underground near water and soil?", "plump helmet man")
    addq("What is a floating pod with eye-stalks which can spray poison and it gives off poison gas when punctured?", "cave floater")
    addq("What is a small, round humanoid found wandering the caves deep underground with most of its body is taken up by a huge tusked mouth?", "gorlak")
    addq("What is living gabbro in the shape of a man which are found deep underground?", "elementman gabbro")
    addq("What is a humanoid monster found lurking far underground which feigns death, usually near water, until a victim passes by which then uses its long arms to drag its prey into the water to drown or strangle them?", "reacher")
    addq("What is a gigantic monster, once a dragon, now adapted to and polluted by the underground which's wings fall limp at its side which's face is full of incredibly long teeth which's eyes are large to penetrate the darkness?", "cave dragon")
    addq("What is a huge emaciated-looking bear with great drooping ears and many sharp teeth which is found deep underground?", "blind cave bear")
    addq("What is a small creature that lives in watery ditches deep underground which has a sharp beak and four tentacles with claws at the end?", "pond grabber")
    addq("What is a huge monster that lurks in caverns deep under the earth which uses its wide beak to reach down and pluck up unsuspecting intruders?", "jabberer")
    addq("What is a hideous monster that has the body of a giant mole-rat and the torso of a mole-rat man which is found deep underground?", "molemarian")
    addq("What is a creature that crawls along the cavern ceiling with four long arms which's body is shaped as the head of a man with a mouth full of shark teeth which waits for its prey to pass below?", "manera")
    addq("What is a small bat-like creature with the head of an insect which is found deep underground?", "bugbat")
    addq("What is a man-shaped abomination made entirely of blood which are only found very near the underworld?", "blood man")
    addq("What is a gigantic version of its tiny cousin, this long, slimy creature tunnels through the rocks deep underground?", "giant earthworm")
    addq("What is a large, long-bodied grazer with a thick mane that feeds on the tops of towercap mushrooms deep under the earth?", "draltha")
    addq("What is a tiny underground creature made of a mass of appendages resembling human fingers which creeps across the ground like a starfish and eats with a mouth on the bottom of its body?", "creepy crawler")
    addq("What is a huge monster with an enormous tail, covered with thick fur which run on four legs and can be found deep under the earth?", "rutherer")
    addq("What is a medium-sized monster walking on two clawed legs which has two mouths on the ends of a pair of tentacles which uses its mouths to digest its victims with acid and rows of razor-like teeth?", "green devourer")
    addq("What is a snake-like creature living deep underground which's head is covered in armor so that is resembles the head of a dragon?", "helmet snake")
    addq("What is a large creature found grazing on mushrooms deep underground which walks on two legs and has the head of a bird with the antlers of a great elk?", "elk bird")
    addq("What is a large ball of skin found moving around the debris near underground ponds which is there that it absorbs dead matter for food?", "flesh ball")
    addq("What is a fearsome, long-toothed mouth the size of a man's head, flying on bat wings which is found in deep caves?", "hungry head")
    addq("What is a tiny underground monster with large claws and horns which walks on two legs and is dangerous when encountered in large numbers?", "crundle")
    addq("What is a small rock-eating creature that lives in molten rock which scurries on little feet and swims through liquid rock with sharp wings which uses magma to digest rock and spits out burning globs?", "magma crab")
    addq("What is a tiny amphibian with a long prehensile tail which lives in underground swamps and tower-cap forests on which it feeds?", "cap hopper")
    addq("What is a large cavern-dwelling humanoid monster which has a gaping mouth with many sharp teeth which has no eyes and only two digits on each hand and foot?", "blind cave ogre")
    addq("What is a huge cave monster with hundreds of feet moving along the bottom of its long body with in place of a head, it has an enormous toothy maw?", "voracious cave crawler")
    addq("What is a small underground monster that crawls across the cavern wall with its four clawed hands which has a single large eye which can shine with its own light, otherwise its stony skin blends in with the rock which has no mouth and is said to feed on evil alone?", "creeping eye")
    addq("What is a large quadruped with a mane circling its manlike face and hands at the end of its forelimbs which lives underground and is fond of raiding the supplies of cavern outposts?", "drunian")
    addq("What is a transparent and amorphous monster that lives underground which is small in size and is found crawling across the cavern floor which's organs appear to be floating inside of its body?", "floating guts")

    addq("What is a huge monster in the shape of a nautilus?", "giant nautilus")
    addq("What is a person with the shell and tentacles of a nautilus?", "nautilus man")
    addq("What is a tiny, mollusk with a large shell and many tentacles?", "nautilus")
    addq("What is a huge monster in the shape of a harp seal?", "giant harp seal")
    addq("What is a person with the head and flippers of a harp seal?", "harp seal man")
    addq("What is a small marine mammal which's young are prized for their white fur?", "harp seal")
    addq("What is a huge monster in the shape of an elephant seal?", "giant elephant seal")
    addq("What is a person with the head and flippers of an elephant seal?", "elephant seal man")
    addq("What is a large, predatory marine mammal?", "elephant seal")
    addq("What is a gigantic monster in the shape of a sperm whale?", "giant sperm whale")
    addq("What is a huge person with the head and flippers of a sperm whale?", "sperm whale man")
    addq("What is a giant marine mammal with a toothy jaw?", "sperm whale")
    addq("What is a huge monster in the form of a horseshoe crab?", "giant horseshoe crab")
    addq("What is a person with the head, shell, and tail of a horseshoe crab?", "horseshoe crab man")
    addq("What is a tiny sea animal that lives in the sand just offshore which has a flat body with legs underneath?", "horseshoe crab")     
    addq("What is a huge immobile sponge?", "giant sponge")
    addq("What is a person in the form of a sponge with arms and legs?", "sponge man")
    addq("What is a tiny sea creature which dwells on the ocean floor, devoid of senses or motion?", "sponge")
    addq("What is a gigantic monster in the shape of an orca?", "giant orca")
    addq("What is an aquatic person in the shape of an orca with arms?", "orca man")
    addq("What is a huge ocean mammal which is a vicious predator and can hunt in groups?", "orca")
    addq("What is a huge sea monster in the shape of a cuttlefish?", "giant cuttlefish")
    addq("What is a person with a cuttlefish in place of a head?", "cuttlefish man")
    addq("What is a tiny sea mollusk which can change color and skin patterns for communication?", "cuttlefish")
    addq("What is a giant monster in the form of a leopard seal?", "giant leopard seal")
    addq("What is a legless person with the head and back flippers of a leopard seal?", "leopard seal man")
    addq("What is a large predatory amphibious mammal which is difficult to evade once in the water?", "leopard seal")
    addq("What is a large monster in the shape of a crab?", "giant crab")
    addq("What is a person with the head and pincers of a crab?", "crab man")
    addq("What is a tiny shelled ocean creature with many long legs which has two large pincers on its front limbs?", "crab")
    addq("What is a dangerous water monster known for attacking ships at sea?", "giant octopus")
    addq("What is a person with an octopus in place of a head?", "octopus man")
    addq("What is a medium-sized underwater mollusk with eight arms which is the most clever of its kind?", "octopus")

    addq("What is a tiny insect with a pulsating, lumpy body which is an evil bug that seeks blood?", "blood gnat")
    addq("What is an insect many times the size of its peers which is known for its deafening buzz?", "acorn fly")
    addq("What is a tiny translucent creature, found in evil forests?", "phantom spider")
    addq("What is a tiny creature made up of a series of crackling knobs set at strange angles?", "knuckle worm")
    addq("What is a tiny reptile, running on two legs which has a horn on the end of its nose?", "two legged rhino lizard")
    addq("What is a fluffy, pudge-filled being, known for its warm heart and stumble bumblings?", "fluffy wambler")
    addq("What is an insidious form of vermin which lives only to steal food from others?", "rat demon")
    addq("What is a small mud-dwelling amphibian?", "moghopper")
    addq("What is a small mammal noted for its tenacity which has long ears and flashing eyes?", "foxsquirrel")

    addq("What is a huge monster in the shape of an iguana?", "giant iguana")
    addq("What is a person with the head and tail of an iguana?", "iguana man")
    addq("What is a relatively large arboreal lizard found in the tropical forests which though is a vegetarian, and mainly docile, it may whip with its extremely long tail when angered?", "iguana")
    addq("What is a large monster in the shape of an anole?", "giant anole")
    addq("What is a person with the head and tail of an anole?", "anole man")
    addq("What is a small lizard with adhesive feet for climbing which can change color from brown to green to fit its surroundings?", "anole")
    addq("What is a large monster in the shape of a chameleon?", "giant chameleon")
    addq("What is a colorful person with the head and tail of a chameleon?", "chameleon man")
    addq("What is a colorful lizard that spends its life hunting insects with its long tongue which moves slowly through the trees, spying the surroundings with its independently roving eyes?", "chameleon")
    addq("What is a large monster in the shape of a skink?", "giant skink")
    addq("What is a long-bodied person with the head and tail of a skink?", "skink man")
    addq("What is a relatively large lizard which can be found in most climates, foraging for bugs during daylight hours?", "skink")
    addq("What is a huge monster in the shape of a lizard?", "giant lizard")
    addq("What is a person with the head and tail of a lizard?", "lizard man")
    addq("What is a small reptile?", "lizard")

    addq("What is a huge monster shaped like a pond turtle?", "giant pond turtle")
    addq("What is a person with the head and shell of a pond turtle?", "pond turtle man")
    addq("What is a tiny reptile with a shell on its back which can be found in rivers and ponds?", "pond turtle")
    addq("What is a huge monster in the form of a mink?", "giant mink")
    addq("What is a person with the head and tail of a mink?", "mink man")
    addq("What is a small, predatory, weasel-like mammal which is also semi-aquatic?", "mink")
    addq("What is a large monster in the shape of an axolotl?", "giant axolotl")
    addq("What is a person with the head and tail of an axolotl?", "axolotl man")
    addq("What is a small salamander found in remote lakes which has the mysterious ability to regrow limbs?", "axolotl")
    addq("What is a large monster in the shape of a leech?", "giant leech")
    addq("What is a large slug-like creature with the torso of a man which's face is a mockery of teeth and slime?", "leech man")
    addq("What is a tiny, aquatic, worm-like creature that feeds on blood?", "leech")
    addq("What is a large river monster, known for building huge wooden fortresses?", "giant beaver")
    addq("What is a person with the head and flat tail of a beaver?", "beaver man")
    addq("What is a small river mammal with a flat tail, known for building wooden dams?", "beaver")
    addq("What is a large monster with an enormous shell and immensely powerful jaw?", "giant snapping turtle")
    addq("What is a person with the shell and head of a snapping turtle?", "snapping turtle man")
    addq("What is a large reptile with a thick ridged shell which has been known to consume snakes and smaller turtles, and its bite can amputate fingers?", "snapping turtle")
    addq("What is a medium-sized reptile with a thick shell, which it can retreat into when threatened which can administer a painful bite?", "snapping turtle")
    addq("What is a large monster in the form of an otter?", "giant otter")
    addq("What is a person with the long body and head of an otter?", "otter man")
    addq("What is a small marine mammal with a long body which enjoy eating shellfish and other small animals?", "sea otter")
    addq("What is a small river mammal with a long body which enjoy eating shellfish and other small animals?", "river otter")

    addq("What is a large monster taking the shape of a flying squirrel?", "giant flying squirrel")
    addq("What is a person with the head and wings of a flying squirrel?", "flying squirrel man")
    addq("What is a tiny grey rodent that is only active at night which can sail between trees on wings stretching between its front and hind legs?", "flying squirrel")
    addq("What is a large monster with the shape of a hedgehog?", "giant hedgehog")
    addq("What is a person with the head and spines of a hedgehog?", "hedgehog man")
    addq("What is a small round mammal whose back is covered in spines which is nocturnal and feeds on insects which curls into a ball when startled and is found in temperate regions?", "hedgehog")
    addq("What is a large creature the shape of a hamster?", "giant hamster")
    addq("What is a person with the head and fur of a hamster?", "hamster man")
    addq("What is a tiny rodent that burrows by day and scurries about at night?", "hamster")

    addq("What is a large creature the shape of a chipmunk?", "giant chipmunk")
    addq("What is a striped person with the head and tail of a chipmunk?", "chipmunk man")
    addq("What is a tiny striped rodent found scurrying through the bushes and trees of the temperate forest?", "chipmunk")
    addq("What is a large creature the shape of a red squirrel?", "giant red squirrel")
    addq("What is a person with the head and tail of a red squirrel?", "red squirrel man")
    addq("What is a small red rodent found in the trees of temperate woodlands?", "red squirrel")
    addq("What is a large creature the shape of a gray squirrel?", "giant grey squirrel")
    addq("What is a person with the head and tail of a gray squirrel?", "grey squirrel man")
    addq("What is a small grey rodent found chirping in the trees of temperate woodlands?", "grey squirrel")
    addq("What is a person with the head and tail of a rat?", "rat man")
    addq("What is a small, intelligent vermin with a long naked tail?", "rat")

    addq("What is a huge sea monster the shape of a squid?", "gigantic squid")
    addq("What is a small person with a head bearing ten tentacles?", "squid man")
    addq("What is a tiny sea vermin with eight arms and two tentacles which can spray ink to confuse predators?", "squid")
    addq("What is an invertebrate found off the coast which has a sting which can be severe?", "sea nettle jellyfish")
    addq("What is a medium-sized oceanic fish prized for its meat?", "mackerel")
    addq("What is a small flat fish found in the muddy bottom of coastal run-offs and ponds?", "flounder")
    addq("What is a small flat fish found on the muddy bottom of shallow seas?", "sole")
    addq("What is a small, round, brightly-colored fish found in coral reefs?", "white spotted puffer")
    addq("What is a small, nocturnal, marine fish which can be found hunting in coral reefs?", "glasseye")
    addq("What is a tiny, curved and colorful fish found in coral reefs?", "seahorse")
    addq("What is an oceanic fish?", "hake")
    addq("What is a medium-sized fish found in tributaries and oceans?", "steelhead trout")
    addq("What is a tiny blue-green oceanic fish, found only in temperate waters?", "anchovy")
    addq("What is a small marine fish that travels to rivers to breed?", "shad")
    addq("What is a tiny marine fish found in vast schools?", "herring")
    addq("What is a small, shark-like creature that lives in the ocean's muddy shallows which's skin sparkles and it has a venomous spine on its back?", "spotted ratfish")
    addq("What is a small winged fish found in shallow seas?", "thornback ray")
    addq("What is a medium-sized, winged fish found in the muddy coasts of both temperate and tropical waters?", "bat ray")
    addq("What is a small, jawless, filter-feeding fish found in brooks and streams?", "brook lamprey")
    addq("What is a small, spineless, eel-like fish that lives on the bottom of the ocean which can turn the water around its body into a cloud of slime to escape predators?", "hagfish")
    addq("What is a tiny orange marine fish that lives inside the tentacles of a poisonous invertebrate?", "clownfish")
    addq("What is a medium-sized red fish that lives in the ocean and swims up a river to breed?", "salmon")
    addq("What is a small marine creature that lives in a shell rooted to the sea floor?", "oyster")
    addq("What is a small creature found in both salt and fresh water that lives in an asymmetrical shell rooted to the bottom?", "mussel")

    addq("What is a small striped fish found in fresh water?", "perch")
    addq("What is a tiny colorful fish found in tropical lakes and rivers?", "guppy")
    addq("What is a tiny spotted fish found in coastal rivers and temperate lakes?", "sailfin molly")
    addq("What is a medium-sized spotted fish found in temperate rivers and lakes?", "rainbow trout")
    addq("What is a medium-sized spotted fish found in temperate lakes and rivers?", "char")
    addq("What is a small spotted fish found in tropical rivers and lakes?", "banded knifefish")
    addq("What is a small whiskered fish found in inland waters?", "black bullhead")
    addq("What is a small whiskered fish found scavenging in inland waters?", "yellow bullhead")
    addq("What is a small whiskered fish found in muddy inland waters?", "brown bullhead")
    addq("What is a tiny orange-striped fish which lives in inland waters?", "clown loach")
    addq("What is a small fish which can walk on the land and breathe air which burrows in the mud when things get dry?", "lungfish")

    addq("What is a bird of prey so large and ferocious it dwarfs many dragons with all beneath its mighty wings should fear the sky?", "roc")
    addq("What is a giant creature with many eyes and arms to terrify the sea?", "sea monster")
    addq("What is a giant limbless dragon that lives in the sea?", "sea serpent")
    addq("What is a man-like creature with the tail of a fish instead of legs?", "merperson")
    addq("What is a giant dragon-like monster with seven biting heads?", "hydra")
    addq("What is a monster in the shape of a woman with a bird's wings in place of arms and talons for feet?", "harpy")
    addq("What is a flying monster with stretched skin over its emaciated body which has the head of a jackal with needle-like horns protruding through its mane?", "nightwing")
    addq("What is a large, four-armed ape creature with three eyes and razor-sharp teeth?", "trangler")
    addq("What is a man-shaped creature with the legs of a goat and the empty-eyed skull of a goat?", "blendec foul")
    addq("What is an evil monster from the swamp which resembles a knot of waterlogged weeds but will strike the unaware victim?", "grimeling")
    addq("What is a creature from the evil swamp which resembles a squat, wingless bird with powerful beak and legs which's blotchy skin is brightly colored?", "beak dog")
    addq("What is a tiny winged humanoid with shifting colors which performs intricate aerial dances in large groups?", "pixie")
    addq("What is a tiny, giggling humanoid with lacy wings?", "fairy")
    addq("What is a fierce creature from the evil snowy wilds which has white fur and a piercing howl?", "ice wolf")
    addq("What is a large humanoid monster from the wild tundra which has translucent skin, icicles for teeth, red glowing eyes and pointed ears?", "blizzard man")
    addq("What is a large and mysterious ape-like creature found in temperate forests?", "sasquatch")
    addq("What is a large ape-like creature with white fur, found in the snowy wilds?", "yeti")
    addq("What is a giant humanoid monster with the head of a bull?", "minotaur")
    addq("What is a giant humanoid monster with two heads?", "ettin")
    addq("What is a giant humanoid monster with a single eye set in its forehead?", "cyclops")
    addq("What is a gigantic creature resembling a human, almost unparalleled in size?", "giant")
    addq("What is a gigantic magic statue made of bronze and bent on mayhem?", "bronze colossus")
    addq("What is a medium-sized humanoid with the horns and legs of a goat?", "satyr")
    addq("What is a gigantic reptilian creature which is magical and can breathe fire which can live for thousands of years?", "dragon")
    addq("What is a horse-like creature with a spiral horn growing from its forehead?", "unicorn")
    addq("What is a giant humanoid monster found stomping about in the evil plains which's low howls can be heard long before they are seen?", "ogre")
    addq("What is a huge humanoid monster with coarse fur, large tusks and horns?", "troll")
    addq("What is a small humanoid creature with a mischievous, toothy grin?", "gremlin")
    addq("What is a small, squat humanoid with large pointy ears and yellow glowing eyes?", "kobold")
    addq("What is a medium-sized humanoid driven to cruelty by its evil nature?", "goblin")
    addq("What is a medium-sized creature dedicated to the ruthless protection of nature?", "elf")
    addq("What is a medium-sized creature prone to great ambition?", "human")

    addq("What is an evil humanoid with a long tail, black spiky fur and a twitching nose which lives far underground?", "rodent man")
    addq("What is a humanoid with the head and body of an ant?", "ant man")
    addq("What is a large white snake with the arms and torso of a man which are evil and live far underground?", "serpent man") 
    addq("What is tese creatures are shaped like men covered with rough scales which have the head and tail of a lizard and possess a dark and evil intelligence which are found deep under the earth?", "reptile man")
    addq("What is tese evil creatures resemble walking frogs with arms and the intelligence to use them which live in the waters far under the earth?", "amphibian man")
    addq("What is a gigantic blue and orange bird?", "giant cave swallow")
    addq("What is a feathered man with the wings and head of a bird which lives underground?", "cave swallow man")
    addq("What is a small blue and orange bird?", "cave swallow")
    addq("What is a humanoid made of mud which lives near water underground?", "mud lementman")
    addq("What is a man-shaped creature made of iron?", "iron lementman")
    addq("What is magma moving in the shape of a man which has a cracked black crust?", "magma lementman")
    addq("What is fire in the shape of a human that can hurl fireballs?", "fire lementman")
    addq("What is a tiny larva which is prized for its milk?", "purring maggot")
    addq("What is a humanoid with the head of a bat and wings stretching from wrist to ankle?", "bat man")
    addq("What is a tiny winged creature that hunts at night and rests in caves during the day?", "bat")
    addq("What is an animal person with the head of the amphibious olm which lives underground near water?", "olm man")
    addq("What is a tiny amphibian, found in underground streams?", "olm")
    addq("What is a serpent made of pure fire which can inject liquid fire as venom?", "fire snake")
    addq("What is a small, pale arthropod found in underground streams and ponds?", "lobster cave")
    addq("What is a humanoid creature with the head of a blind cave fish which live in colonies in watery regions far underground?", "cave fish man")
    addq("What is a small pale creature found in underground streams and ponds?", "cave fish")
    addq("What is a tiny underground bug, sought after for its thread?", "cave spider")
    addq("What is a large underground monster with eight legs and sharp, venomous fangs?", "giant cave spider")
    addq("What is a small humanoid surrounded by fire which they can hurl at their enemies?", "fire imp")
    addq("What is a gigantic digging creature found underground?", "giant mole")
    addq("What is a savage man-like cave creature?", "troglodyte")
    addq("What is a large, pale rodent with loose, hanging, hairless skin which has long teeth and an incredibly powerful bite which is found underground?", "naked dog mole")
    addq("What is a huge rodent found underground?", "large rat")
    addq("What is a gigantic rodent found underground?", "giant rat")
    addq("What is a giant flying mammal found underground?", "giant bat")
    addq("What is a giant amphibian predator found underground near water?", "giant olm")
    addq("What is a giant amphibian predator found underground?", "giant cave toad")
    addq("What is a huge, predatory reptile with pale, colorless scales and red eyes which lives in caves and ambushes its prey?", "cave crocodile")

    addq("What is a huge monster in the shape of an opossum?", "giant opossum")
    addq("What is a person with the head and tail of an opossum?", "opossum man")
    addq("What is a small mammal resembling a large, white rat?", "opossum")
    addq("What is a huge monster in the form of a coati?", "giant coati")
    addq("What is a person with the head and tail of a coati?", "coati man")
    addq("What is a small, long-nosed raccoon-like creature?", "coati")
    addq("What is a huge monster in the form of a dingo?", "giant dingo")
    addq("What is a person with the head of a dingo?", "dingo man")
    addq("What is a small dog-like creature which are known to attack livestock?", "dingo")
    addq("What is a huge monster in the shape of a wombat?", "giant wombat")
    addq("What is a muscular person with the head of a wombat?", "wombat man")
    addq("What is a small, stocky mammal which is found from the mountains to the woodlands?", "wombat")
    addq("What is a huge monster in the form of an ibex?", "giant ibex")
    addq("What is a horned person with the head of an ibex?", "ibex man")
    addq("What is a small horned mammal which can be found in the mountains leaping from rock to rock?", "ibex")
    addq("What is a huge monster in the form of a copperhead snake?", "giant copperhead snake")
    addq("What is a large copperhead snake with the arms of a man?", "copperhead snake man")
    addq("What is a tiny venomous snake found in the woods and swamps?", "copperhead snake")
    addq("What is a large monster taking the shape of a weasel?", "giant weasel")
    addq("What is a person with the head and tail of a weasel?", "weasel man")
    addq("What is a tiny mammal with a slender body which hunts in mouse holes as well as barn yards?", "weasel")
    addq("What is a huge monster taking the shape of a rattlesnake?", "giant rattlesnake")
    addq("What is a person resembling a large rattlesnake with arms?", "rattlesnake man")
    addq("What is a small reptile with a tell-tale rattle and vicious bite that leads to a quick death?", "rattlesnake")
    addq("What is a large monster in the shape of a hare?", "giant hare")
    addq("What is a long-eared person with the head and tail of a hare?", "hare man")
    addq("What is a swift, long-eared rodent with long legs and a short fluffy tail?", "hare")
    addq("What is a large monster in the shape of a green tree frog?", "giant green tree frog")
    addq("What is a green person with the head of a green tree frog?", "green tree frog man")
    addq("What is a tiny amphibian that lives in the trees?", "green tree frog")
    addq("What is a large monster in the form of a skunk?", "giant skunk")
    addq("What is a striped person with the head and tail of a skunk?", "skunk man")
    addq("What is a small black and white mammal which is capable of spraying a stinking fluid?", "skunk")
    addq("What is a large monster in the form of a bobcat?", "giant bobcat")
    addq("What is a person with the head and short tail of a bobcat?", "bobcat man")
    addq("What is a small feline predator with a shortened tail?", "bobcat")
    addq("What is a huge monster in the shape of a gray langur?", "giant gray langur")
    addq("What is a grey person with the head and tail of a gray langur?", "gray langur man")
    addq("What is a small monkey that can be found in forests and the streets of towns?", "gray langur")
    addq("What is a large monster in the form of a kingsnake?", "giant kingsnake")
    addq("What is a legless person with the head and tail of a kingsnake?", "kingsnake man")
    addq("What is a small, brightly-colored snake which is known for eating other snakes and being mistaken for its venomous cousins?", "kingsnake")
    addq("What is a large monster in the form of a porcupine?", "giant porcupine")
    addq("What is a person with the head and quills of a porcupine?", "porcupine man")
    addq("What is a small rodent covered with sharp quills which eat grass and leaves and can even climb trees?", "porcupine")
    addq("What is a large monster in the shape of an echidna?", "giant echidna")
    addq("What is a spiny person with the head of an echidna?", "echidna man")
    addq("What is a small spiny mammal with a long snout which eats ants and termites and reproduces by laying eggs?", "echidna")
    addq("What is a large monster in the form of an adder?", "giant adder")
    addq("What is a large adder with the torso and arms of a man?", "adder man")
    addq("What is a tiny snake with ridged scales and a powerful venomous bite?", "adder")
    addq("What is a large koala-shaped monster?", "giant koala")
    addq("What is a grey person with the head of a koala?", "koala man")
    addq("What is a small, grey, tree-dwelling creature?", "koala")
    addq("What is a huge monster in the shape of a kangaroo?", "giant kangaroo")
    addq("What is a person with the head and powerful legs of a kangaroo?", "kangaroo man")
    addq("What is a medium-sized creature that can be found hopping through the grassland?", "kangaroo")
    addq("What is a large dog-like monster with a haunting howl?", "giant coyote")
    addq("What is a person with the head and tail of a coyote?", "coyote man")
    addq("What is a medium-sized dog-like creature which is sly, and groups can be heard howling in the night?", "coyote")
    addq("What is a huge monster boar with jagged tusks?", "giant wild boar")
    addq("What is a person with the head of a wild boar?", "wild boar man")
    addq("What is a medium-sized beast, known for its tusks and powerful build?", "wild boar")

    addq("What is a huge monster in the form of a lion tamarin?", "giant lion tamarin")
    addq("What is an orange person with the head and tail of a lion tamarin?", "lion tamarin man")
    addq("What is a small orange monkey with a long tail?", "lion tamarin")
    addq("What is a huge monster in the form of an aardvark?", "giant aardvark")
    addq("What is a person with the head and tail of an aardvark?", "aardvark man")
    addq("What is a small, nocturnal mammal which has a long tongue with which to eat insects?", "aardvark")
    addq("What is a huge monster in the form of an impala?", "giant impala")
    addq("What is a slender, horned man with the head and tail of a impala?", "impala man")
    addq("What is a small, slender gazelle-like creature?", "impala")
    addq("What is a huge monster in the form of a tapir?", "giant tapir")
    addq("What is a person with the head of a tapir?", "tapir man")
    addq("What is a medium-sized mammal with a prehensile nose which lives in the tropical rainforest?", "tapir")
    addq("What is a huge monster in the form of a python?", "giant python")
    addq("What is a large python with arms of a man?", "python man")
    addq("What is a small snake found in the trees which kills its prey by using its long body to constrict them?", "python")
    addq("What is a huge monster in the form of a bushmaster?", "giant bushmaster")
    addq("What is a large bushmaster with the arms of a man?", "bushmaster man")
    addq("What is a tiny venomous snake which is the longest of the pit vipers?", "bushmaster")
    addq("What is a huge monster shaped like an aye-aye?", "giant aye-aye")
    addq("What is a person with the head and fingers of an aye-aye?", "aye-aye man")
    addq("What is a small, nocturnal, tree-dwelling mammal which uses its long fingers to fish out grubs from the wood?", "aye-aye")
    addq("What is a huge monster in the form of a sloth bear?", "giant sloth bear")
    addq("What is a person with the head and claws of a sloth bear?", "sloth bear man")
    addq("What is a medium-sized mammal that lives in the trees which is known for its easy-going nature?", "sloth bear")
    addq("What is a large monster taking the shape of a black mamba?", "giant black mamba")
    addq("What is a person in the form of a large black mamba with arms?", "black mamba man")
    addq("What is a small aggressive snake which can move very quickly which's venom is deadly?", "black mamba")
    addq("What is a huge monster in the form of a pangolin?", "giant pangolin")
    addq("What is a person with the head and scales of a pangolin?", "pangolin man")
    addq("What is a small mammal covered in hard scales which has a long nose and tongue which it uses to feed?", "pangolin")
    addq("What is a large monster in the form of a spider monkey?", "giant spider monkey")
    addq("What is a long-limbed person with the head and tail of a spider monkey?", "spider monkey man")
    addq("What is a small animal found in the canopy of the jungle which have extremely long arms and legs?", "spider monkey")
    addq("What is a huge monster in the shape of a sloth?", "giant sloth")
    addq("What is a person with the head of a sloth?", "sloth man")
    addq("What is a small, slow-moving mammal that lives in the trees?", "sloth")
    addq("What is a large monster in the form of a capuchin?", "giant capuchin")
    addq("What is a person with the head and tail of a capuchin?", "capuchin man")
    addq("What is a tiny diurnal monkey which spends its time in the trees searching for food?", "capuchin")
    addq("What is a large monster in the form of a jackal?", "giant jackal")
    addq("What is a person with the head and tail of a jackal?", "jackal man")
    addq("What is a small wolf-like scavenger which normally found in pairs, can form packs when they find a body?", "jackal")
    addq("What is a huge monster in the shape of an ocelot?", "giant ocelot")
    addq("What is a person with the head and tail of an ocelot?", "ocelot man")
    addq("What is a small cat-like creature found in the jungle?", "ocelot")
    addq("What is a large monster in the shape of a king cobra?", "giant king cobra")
    addq("What is a legless person with the head and tail of a king cobra?", "king cobra man")
    addq("What is a small limbless reptile known for its deadly venom and the warning of its hood?", "king cobra")
    addq("What is a huge monster in the shape of a monitor lizard?", "giant monitor lizard")
    addq("What is a person with the head and tail of a monitor lizard?", "monitor lizard man")
    addq("What is a medium-sized reptile which can be found foraging for food such as eggs or worms which are said to be the most intelligent of their kind?", "monitor lizard")
    addq("What is a huge monster in the form of an anaconda?", "giant anaconda")
    addq("What is a large anaconda with the torso and arms of a man?", "anaconda man")
    addq("What is a medium-sized snake that lives in the trees which eats prey much larger than itself and slays them by crushing them to death?", "anaconda")
    addq("What is a huge monster the shape of a hyena?", "giant hyena")
    addq("What is a person with the head and markings of a hyena?", "hyena man")
    addq("What is a medium-sized pack predator found in the savanna?", "hyena")
    addq("What is a large mongoose-like monster known for hunting people amongst other things?", "giant mongoose")
    addq("What is a small person with the head and tail of a mongoose?", "mongoose man")
    addq("What is a very small mammal with short legs and a long tail which hunts small animals to eat?", "mongoose")

    addq("What is a huge monster in the shape of a lynx?", "giant lynx")
    addq("What is a person with the head and tail of a lynx?", "lynx man")
    addq("What is a medium-sized mammalian predator which is known by the tell-tale tufts of hair on the tips of its ears?", "lynx")
    addq("What is a large monster in the shape of a stoat?", "giant stoat")
    addq("What is a long-bodied person with the head of a stoat?", "stoat man")
    addq("What is a small weasel-like creature that hunts rodents and preys on the nests of birds?", "stoat")

"""
 which
"""
players = int(input("The number of players: "))
p = []
for i in range(players):
    p.append(input(f"Enter player {i + 1}'s name: "))
p.sort()
for i in range(len(p)):
    p[i] = p[i].title()
qn = 0
pp = []
for i in p:
    pp.append(0)
if what == 2 or what == 3:
    easy = input("Enable easy mode? (y/n) ")
    if "y" in easy.lower():
        easy = True
        print("Easy mode enabled.")
    else:
        easy = False
while True:
    if len(q) == 0:
        print("Game ended.")
        print("Final scores: ")
        for i in range(len(p)):
            print(f"{p[i]}:\t\t{pp[i]} Points")
        input()
        quit()
    qn += 1
    rand = randint(1, len(q))
    qr = q[rand]
    ar = a[rand]
    if not(easy):
        while ar.startswith("giant ") or ar.endswith(" man"):
            if ar.startswith("giant ") or ar.endswith(" man"):
                del q[rand]
                del a[rand]
            rand = randint(1, len(q))
            qr = q[rand]
            ar = a[rand]
    print(f"Question #{qn}: {qr}")
    pa = []
    for i in p:
        pa.append(input(f"{i}'s answer: "))
    try:
        ar = float(ar)
        flt = True
    except Exception:
        flt = False
    try:
        ar = float(ar)
        input(f"The answer was {ar}.")
    except Exception:
        input(f"The answer was {ar.strip(".")}.")
    if flt:
        for i in range(len(p)):
            answer = float(pa[i])
            fark = abs(ar - answer)
            if fark < 0:
                fark = 0
            print(f"{p[i]} guessed ~{int(fark)} numbers away from the answer. (~{int(100 - fark)} points)")
        input()
        for i in range(len(p)):
            answer = pa[i]
            pp[i] += 100 - fark
            print(f"{p[i]}:\t\t{pp[i]} Points")
        input()
    else:
        correct = []
        for i in range(len(p)):
            answer = pa[i]
            if answer.lower() == ar.lower():
                print(f"{p[i]} guessed correctly. (100 points)")
                correct.append(100)
            elif ar.lower() in answer.lower():
                print(f"{p[i]} guessed near correct. (60 points)")
                correct.append(60)
            elif answer.lower() in ar.lower():
                print(f"{p[i]} guessed near correct. (30 points)")
                correct.append(30)
            else:
                print(f"{p[i]} guessed incorrectly. (0 points)")
                correct.append(0)
        input()
        for i in range(len(p)):
            pp[i] += correct[i]
            print(f"{p[i]}:\t\t{pp[i]} Points")
        input()
    del q[rand], a[rand]
