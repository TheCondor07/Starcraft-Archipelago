import logging

from BaseClasses import Item


def ItemFactory(items, player):
    ret = []
    singleton = False
    if isinstance(items, str):
        items = [items]
        singleton = True
    for item in items:
        if item in item_table:
            advancement, priority, type, code, pedestal_hint, pedestal_credit, sickkid_credit, zora_credit, witch_credit, fluteboy_credit, hint_text = item_table[item]
            ret.append(Item(item, advancement, priority, type, code, pedestal_hint, pedestal_credit, sickkid_credit, zora_credit, witch_credit, fluteboy_credit, hint_text, player))
        else:
            logging.getLogger('').warning('Unknown Item: %s', item)
            return None

    if singleton:
        return ret[0]
    return ret


# Format: Name: (Advancement, Priority, Type, ItemCode, Pedestal Hint Text, Pedestal Credit Text, Sick Kid Credit Text, Zora Credit Text, Witch Credit Text, Flute Boy Credit Text, Hint Text)
item_table = {'Bow': (True, False, None, 0x0B, 'You have\nchosen the\narcher class.', 'the stick and twine', 'arrow-slinging kid', 'arrow sling for sale', 'witch and robin hood', 'archer boy shoots again', 'the Bow'),
              'Progressive Bow': (True, False, None, 0x64, 'You have\nchosen the\narcher class.', 'the stick and twine', 'arrow-slinging kid', 'arrow sling for sale', 'witch and robin hood', 'archer boy shoots again', 'a Bow'),
              'Progressive Bow (Alt)': (True, False, None, 0x65, 'You have\nchosen the\narcher class.', 'the stick and twine', 'arrow-slinging kid', 'arrow sling for sale', 'witch and robin hood', 'archer boy shoots again', 'a Bow'),
              'Silver Arrows': (True, False, None, 0x58, 'Do you fancy\nsilver tipped\narrows?', 'and the ganonsbane','ganon-killing kid', 'ganon doom for sale', 'fungus for pork','archer boy shines again', 'the Silver Arrows'),
              'Silver Bow': (True, False, None, 0x3B, 'Buy 1 Silver\nget Archery\nfor free.', 'the baconmaker', 'ganon-killing kid', 'ganon doom for sale', 'fungus for pork', 'archer boy shines again', 'the Silver Bow'),
              'Book of Mudora': (True, False, None, 0x1D, 'This is a\nparadox?!', 'and the story book', 'the scholarly kid', 'moon runes for sale', 'drugs for literacy', 'book-worm boy can read again', 'the Book'),
              'Hammer': (True, False, None, 0x09, 'stop\nhammer time!', 'and m c hammer', 'hammer-smashing kid', 'm c hammer for sale', 'stop...   hammer time', 'stop, hammer time', 'the Hammer'),
              'Hookshot': (True, False, None, 0x0A, 'BOING!!!\nBOING!!!\nBOING!!!', 'and the tickle beam', 'tickle-monster kid', 'tickle beam for sale', 'witch and tickle boy', 'beam boy tickles again', 'the Hookshot'),
              'Magic Mirror': (True, False, None, 0x1A, 'Isn\'t your\nreflection so\npretty?', 'the face reflector', 'the narcissistic kid', 'your face for sale', 'trades looking-glass', 'narcissistic boy is happy again', 'the Mirror'),
              'Flute': (True, False, None, 0x14, 'Save the duck\nand fly to\nfreedom!', 'and the duck call', 'the duck-call kid', 'duck call for sale', 'duck-calls for trade', 'flute boy plays again', 'the Flute'),
              'Pegasus Boots': (True, False, None, 0x4B, 'Gotta go fast!', 'and the sprint shoes', 'the running-man kid', 'sprint shoe for sale', 'shrooms for speed', 'gotta-go-fast boy runs again', 'the Boots'),
              'Power Glove': (True, False, None, 0x1B, 'Now you can\nlift weak\nstuff!', 'and the grey mittens', 'body-building kid', 'lift glove for sale', 'fungus for gloves', 'body-building boy lifts again', 'the Glove'),
              'Cape': (True, False, None, 0x19, 'Wear this to\nbecome\ninvisible!', 'the camouflage cape', 'red riding-hood kid', 'red hood for sale', 'hood from a hood', 'dapper boy hides again', 'the Cape'),
              'Mushroom': (True, False, None, 0x29, 'I\'m a fun guy!\n\nI\'m a funghi!', 'and the legal drugs', 'the drug-dealing kid', 'legal drugs for sale', 'shroom swap', 'shroom boy sells drugs again', 'the Mushroom'),
              'Shovel': (True, False, None, 0x13, 'Can\n   You\n      Dig it?', 'and the spade', 'archaeologist kid', 'dirt spade for sale', 'can you dig it', 'shovel boy digs again', 'the Shovel'),
              'Lamp': (True, False, None, 0x12, 'Baby, baby,\nbaby.\nLight my way!', 'and the flashlight', 'light-shining kid', 'flashlight for sale', 'fungus for illumination', 'illuminated boy can see again', 'the Lamp'),
              'Magic Powder': (True, False, None, 0x0D, 'you can turn\nanti-faeries\ninto faeries', 'and the magic sack', 'the sack-holding kid', 'magic sack for sale', 'the witch and assistant', 'magic boy plays marbles again', 'the Powder'),
              'Moon Pearl': (True, False, None, 0x1F, '  Bunny Link\n      be\n     gone!', 'and the jaw breaker', 'fortune-telling kid', 'lunar orb for sale', 'shrooms for moon rock', 'moon boy plays ball again', 'the Moon Pearl'),
              'Cane of Somaria': (True, False, None, 0x15, 'I make blocks\nto hold down\nswitches!', 'and the red blocks', 'the block-making kid', 'block stick for sale', 'block stick for trade', 'cane boy makes blocks again', 'the Red Cane'),
              'Fire Rod': (True, False, None, 0x07, 'I\'m the hot\nrod. I make\nthings burn!', 'and the flamethrower', 'fire-starting kid', 'rage rod for sale', 'fungus for rage-rod', 'firestarter boy burns again', 'the Fire Rod'),
              'Flippers': (True, False, None, 0x1E, 'fancy a swim?', 'and the toewebs', 'the swimming kid', 'finger webs for sale', 'shrooms let you swim', 'swimming boy swims again', 'the Flippers'),
              'Ice Rod': (True, False, None, 0x08, 'I\'m the cold\nrod. I make\nthings freeze!', 'and the freeze ray', 'the ice-bending kid', 'freeze ray for sale', 'fungus for ice-rod', 'ice-cube boy freezes again', 'the Ice Rod'),
              'Titans Mitts': (True, False, None, 0x1C, 'Now you can\nlift heavy\nstuff!', 'and the golden glove', 'body-building kid', 'carry glove for sale', 'fungus for bling-gloves', 'body-building boy has gold again', 'the Mitts'),
              'Bombos': (True, False, None, 0x0F, 'Burn, baby,\nburn! Fear my\nring of fire!', 'and the swirly coin', 'coin-collecting kid', 'swirly coin for sale', 'shrooms for swirly-coin', 'medallion boy melts room again', 'Bombos'),
              'Ether': (True, False, None, 0x10, 'This magic\ncoin freezes\neverything!', 'and the bolt coin', 'coin-collecting kid', 'bolt coin for sale', 'shrooms for bolt-coin', 'medallion boy sees floor again', 'Ether'),
              'Quake': (True, False, None, 0x11, 'Maxing out the\nRichter scale\nis what I do!', 'and the wavy coin', 'coin-collecting kid', 'wavy coin for sale', 'shrooms for wavy-coin', 'medallion boy shakes dirt again', 'Quake'),
              'Bottle': (True, False, None, 0x16, 'Now you can\nstore potions\nand stuff!', 'and the terrarium', 'the terrarium kid', 'terrarium for sale', 'special promotion', 'bottle boy has terrarium again', 'a bottle'),
              'Bottle (Red Potion)': (True, False, None, 0x2B, 'Hearty red goop!', 'and the red goo', 'the liquid kid', 'potion for sale', 'free samples', 'bottle boy has red goo again', 'a bottle'),
              'Bottle (Green Potion)': (True, False, None, 0x2C, 'Refreshing green goop!', 'and the green goo', 'the liquid kid', 'potion for sale', 'free samples', 'bottle boy has green goo again', 'a bottle'),
              'Bottle (Blue Potion)': (True, False, None, 0x2D, 'Delicious blue goop!', 'and the blue goo', 'the liquid kid', 'potion for sale', 'free samples', 'bottle boy has blue goo again', 'a bottle'),
              'Bottle (Fairy)': (True, False, None, 0x3D, 'Save me and I will revive you', 'and the captive', 'the tingle kid','hostage for sale', 'fairy dust and shrooms', 'bottle boy has friend again', 'a bottle'),
              'Bottle (Bee)': (True, False, None, 0x3C, 'I will sting your foes a few times', 'and the sting buddy', 'the beekeeper kid', 'insect for sale', 'shroom pollenation', 'bottle boy has mad bee again', 'a bottle'),
              'Bottle (Good Bee)': (True, False, None, 0x48, 'I will sting your foes a whole lot!', 'and the sparkle sting', 'the beekeeper kid', 'insect for sale', 'shroom pollenation', 'bottle boy has beetor again', 'a bottle'),
              'Master Sword': (True, False, 'Sword', 0x50, 'I beat barries and pigs alike', 'and the master sword', 'sword-wielding kid', 'glow sword for sale', 'fungus for blue slasher', 'sword boy fights again', 'the Master Sword'),
              'Tempered Sword': (True, False, 'Sword', 0x02, 'I stole the\nblacksmith\'s\njob!', 'the tempered sword', 'sword-wielding kid', 'flame sword for sale', 'fungus for red slasher', 'sword boy fights again', 'the Tempered Sword'),
              'Fighter Sword': (True, False, 'Sword', 0x49, 'A pathetic\nsword rests\nhere!', 'the tiny sword', 'sword-wielding kid', 'tiny sword for sale', 'fungus for tiny slasher', 'sword boy fights again', 'the Small Sword'),
              'Golden Sword': (True, False, 'Sword', 0x03, 'The butter\nsword rests\nhere!', 'and the butter sword', 'sword-wielding kid', 'butter for sale', 'cap churned to butter', 'sword boy fights again', 'the Golden Sword'),
              'Progressive Sword': (True, False, 'Sword', 0x5E, 'a better copy\nof your sword\nfor your time', 'the unknown sword', 'sword-wielding kid', 'sword for sale', 'fungus for some slasher', 'sword boy fights again', 'a Sword'),
              'Progressive Glove': (True, False, None, 0x61, 'a way to lift\nheavier things', 'and the lift upgrade', 'body-building kid', 'some glove for sale', 'fungus for gloves', 'body-building boy lifts again', 'a Glove'),
              'Green Pendant': (True, False, 'Crystal', (0x04, 0x38, 0x62, 0x00, 0x69, 0x01), None, None, None, None, None, None, None),
              'Blue Pendant': (True, False, 'Crystal', (0x02, 0x34, 0x60, 0x00, 0x69, 0x02), None, None, None, None, None, None, None),
              'Red Pendant': (True, False, 'Crystal', (0x01, 0x32, 0x60, 0x00, 0x69, 0x03), None, None, None, None, None, None, None),
              'Triforce': (True, False, None, 0x6A, '\n   YOU WIN!', 'and the triforce', 'victorious kid', 'victory for sale', 'fungus for the win', 'greedy boy wins game again', 'the Triforce'),
              'Power Star': (True, False, None, 0x6B, 'a small victory', 'and the power star', 'star-struck kid', 'star for sale', 'see stars with shroom', 'mario powers up again', 'a Power Star'),
              'Triforce Piece': (True, False, None, 0x6C, 'a small victory', 'and the thirdforce', 'triangular kid', 'triangle for sale', 'fungus for triangle', 'wise boy has triangle again', 'a Triforce Piece'),
              'Crystal 1': (True, False, 'Crystal', (0x02, 0x34, 0x64, 0x40, 0x7F, 0x06), None, None, None, None, None, None, None),
              'Crystal 2': (True, False, 'Crystal', (0x10, 0x34, 0x64, 0x40, 0x79, 0x06), None, None, None, None, None, None, None),
              'Crystal 3': (True, False, 'Crystal', (0x40, 0x34, 0x64, 0x40, 0x6C, 0x06), None, None, None, None, None, None, None),
              'Crystal 4': (True, False, 'Crystal', (0x20, 0x34, 0x64, 0x40, 0x6D, 0x06), None, None, None, None, None, None, None),
              'Crystal 5': (True, False, 'Crystal', (0x04, 0x32, 0x64, 0x40, 0x6E, 0x06), None, None, None, None, None, None, None),
              'Crystal 6': (True, False, 'Crystal', (0x01, 0x32, 0x64, 0x40, 0x6F, 0x06), None, None, None, None, None, None, None),
              'Crystal 7': (True, False, 'Crystal', (0x08, 0x34, 0x64, 0x40, 0x7C, 0x06), None, None, None, None, None, None, None),
              'Single Arrow': (False, False, None, 0x43, 'a lonely arrow\nsits here.', 'and the arrow', 'stick-collecting kid', 'sewing needle for sale', 'fungus for arrow', 'archer boy sews again', 'an arrow'),
              'Arrows (10)': (False, False, None, 0x44, 'This will give\nyou ten shots\nwith your bow!', 'and the arrow pack', 'stick-collecting kid', 'sewing kit for sale', 'fungus for arrows', 'archer boy sews again', 'ten arrows'),
              'Arrow Upgrade (+10)': (False, False, None, 0x54, 'increase arrow\nstorage, low\nlow price', 'and the quiver', 'quiver-enlarging kid', 'arrow boost for sale', 'witch and more skewers', 'upgrade boy sews more again', 'arrow capacity'),
              'Arrow Upgrade (+5)': (False, False, None, 0x53, 'increase arrow\nstorage, low\nlow price', 'and the quiver', 'quiver-enlarging kid', 'arrow boost for sale', 'witch and more skewers', 'upgrade boy sews more again', 'arrow capacity'),
              'Single Bomb': (False, False, None, 0x27, 'I make things\ngo BOOM! But\njust once.', 'and the explosion', 'the bomb-holding kid', 'firecracker for sale', 'blend fungus into bomb', '\'splosion boy explodes again', 'a bomb'),
              'Bombs (3)': (False, False, None, 0x28, 'I make things\ngo triple\nBOOM!!!', 'and the explosions', 'the bomb-holding kid', 'firecrackers for sale', 'blend fungus into bombs', '\'splosion boy explodes again', 'three bombs'),
              'Bombs (10)': (False, False, None, 0x31, 'I make things\ngo BOOM! Ten\ntimes!', 'and the explosions', 'the bomb-holding kid', 'firecrackers for sale', 'blend fungus into bombs', '\'splosion boy explodes again', 'ten bombs'),
              'Bomb Upgrade (+10)': (False, False, None, 0x52, 'increase bomb\nstorage, low\nlow price', 'and the bomb bag', 'boom-enlarging kid', 'bomb boost for sale', 'the shroom goes boom', 'upgrade boy explodes more again', 'bomb capacity'),
              'Bomb Upgrade (+5)': (False, False, None, 0x51, 'increase bomb\nstorage, low\nlow price', 'and the bomb bag', 'boom-enlarging kid', 'bomb boost for sale', 'the shroom goes boom', 'upgrade boy explodes more again', 'bomb capacity'),
              'Blue Mail': (False, True, None, 0x22, 'Now you\'re a\nblue elf!', 'and the banana hat', 'the protected kid', 'banana hat for sale', 'the clothing store', 'tailor boy banana hatted again', 'the Blue Mail'),
              'Red Mail': (False, True, None, 0x23, 'Now you\'re a\nred elf!', 'and the eggplant hat', 'well-protected kid', 'purple hat for sale', 'the nice clothing store', 'tailor boy fears nothing again', 'the Red Mail'),
              'Progressive Armor': (False, True, None, 0x60, 'time for a\nchange of\nclothes?', 'and the unknown hat', 'the protected kid', 'new hat for sale', 'the clothing store', 'tailor boy has threads again', 'some armor'),
              'Blue Boomerang': (True, False, None, 0x0C, 'No matter what\nyou do, blue\nreturns to you', 'and the bluemarang', 'the bat-throwing kid', 'bent stick for sale', 'fungus for puma-stick', 'throwing boy plays fetch again', 'the Blue Boomerang'),
              'Red Boomerang': (True, False, None, 0x2A, 'No matter what\nyou do, red\nreturns to you', 'and the badmarang', 'the bat-throwing kid', 'air foil for sale', 'fungus for return-stick', 'magical boy plays fetch again', 'the Bed Boomerang'),
              'Blue Shield': (False, True, None, 0x04, 'Now you can\ndefend against\npebbles!', 'and the stone blocker', 'shield-wielding kid', 'shield for sale', 'fungus for shield', 'shield boy defends again', 'the Blue Shield'),
              'Red Shield': (False, True, None, 0x05, 'Now you can\ndefend against\nfireballs!', 'and the shot blocker', 'shield-wielding kid', 'fire shield for sale', 'fungus for fire shield', 'shield boy defends again', 'the Red Shield'),
              'Mirror Shield': (True, False, None, 0x06, 'Now you can\ndefend against\nlasers!', 'and the laser blocker', 'shield-wielding kid', 'face shield for sale', 'fungus for face shield', 'shield boy defends again', 'the Mirror Shield'),
              'Progressive Shield': (True, False, None, 0x5F, 'have a better\nblocker in\nfront of you', 'and the new shield', 'shield-wielding kid', 'shield for sale', 'fungus for shield', 'shield boy defends again', 'a shield'),
              'Bug Catching Net': (True, False, None, 0x21, 'Let\'s catch\nsome bees and\nfaeries!', 'and the bee catcher', 'the bug-catching kid', 'stick web for sale', 'fungus for butterflies', 'wrong boy catches bees again', 'the Bug Net'),
              'Cane of Byrna': (True, False, None, 0x18, 'Use this to\nbecome\ninvincible!', 'and the bad cane', 'the spark-making kid', 'spark stick for sale', 'spark-stick for trade', 'cane boy encircles again', 'the Blue Cane'),
              'Boss Heart Container': (False, False, None, 0x3E, 'Maximum health\nincreased!\nYeah!', 'and the full heart', 'the life-giving kid', 'love for sale', 'fungus for life', 'life boy feels love again', 'a heart'),
              'Sanctuary Heart Container': (False, False, None, 0x3F, 'Maximum health\nincreased!\nYeah!', 'and the full heart', 'the life-giving kid', 'love for sale', 'fungus for life', 'life boy feels love again', 'a heart'),
              'Piece of Heart': (False, False, None, 0x17, 'Just a little\npiece of love!', 'and the broken heart', 'the life-giving kid', 'little love for sale', 'fungus for life', 'life boy feels some love again', 'a heart piece'),
              'Rupee (1)': (False, False, None, 0x34, 'Just pocket\nchange. Move\nright along.', 'the pocket change', 'poverty-struck kid', 'life lesson for sale', 'buying cheap drugs', 'destitute boy has snack again', 'a green rupee'),
              'Rupees (5)': (False, False, None, 0x35, 'Just pocket\nchange. Move\nright along.', 'the pocket change', 'poverty-struck kid', 'life lesson for sale', 'buying cheap drugs', 'destitute boy has snack again', 'a blue rupee'),
              'Rupees (20)': (False, False, None, 0x36, 'Just couch\ncash. Move\nright along.', 'and the couch cash', 'the piggy-bank kid', 'life lesson for sale', 'the witch buying drugs', 'destitute boy has lunch again', 'a red rupee'),
              'Rupees (50)': (False, False, None, 0x41, 'A rupee pile!\nOkay?', 'and the rupee pile', 'the well-off kid', 'life lesson for sale', 'buying okay drugs', 'destitute boy has dinner again', 'fifty rupees'),
              'Rupees (100)': (False, False, None, 0x40, 'A rupee stash!\nHell yeah!', 'and the rupee stash', 'the kind-of-rich kid', 'life lesson for sale', 'buying good drugs', 'affluent boy goes drinking again', 'one hundred rupees'),
              'Rupees (300)': (False, False, None, 0x46, 'A rupee hoard!\nHell yeah!', 'and the rupee hoard', 'the really-rich kid', 'life lesson for sale', 'buying the best drugs', 'fat-cat boy is rich again', 'three hundred rupees'),
              'Rupoor': (False, False, None, 0x59, 'a debt collector', 'and the toll-booth', 'the toll-booth kid', 'double loss for sale', 'witch stole your rupees', 'affluent boy steals rupees', 'a rupoor'),
              'Red Clock': (False, True, None, 0x5B, 'a waste of time', 'the ruby clock', 'the ruby-time kid', 'red time for sale', 'for ruby time', 'moment boy travels time again', 'a red clock'),
              'Blue Clock': (False, True, None, 0x5C, 'a bit of time', 'the sapphire clock', 'sapphire-time kid', 'blue time for sale', 'for sapphire time', 'moment boy time travels again', 'a blue clock'),
              'Green Clock': (False, True, None, 0x5D, 'a lot of time', 'the emerald clock', 'the emerald-time kid', 'green time for sale', 'for emerald time', 'moment boy adjusts time again', 'a red clock'),
              'Single RNG': (False, True, None, 0x62, 'something you don\'t yet have', None, None, None, None, 'unknown boy somethings again', 'a new mystery'),
              'Multi RNG': (False, True, None, 0x63, 'something you may already have', None, None, None, None, 'unknown boy somethings again', 'a total mystery'),
              'Magic Upgrade (1/2)': (True, False, None, 0x4E, 'Your magic\npower has been\ndoubled!', 'and the spell power', 'the magic-saving kid', 'wizardry for sale', 'mekalekahi mekahiney ho', 'magic boy saves magic again', 'Half Magic'),  # can be required to beat mothula in an open seed in very very rare circumstance
              'Magic Upgrade (1/4)': (True, False, None, 0x4F, 'Your magic\npower has been\nquadrupled!', 'and the spell power', 'the magic-saving kid', 'wizardry for sale', 'mekalekahi mekahiney ho', 'magic boy saves magic again', 'Quarter Magic'),  # can be required to beat mothula in an open seed in very very rare circumstance
              'Small Key (Eastern Palace)': (False, False, 'SmallKey', 0xA2, 'A small key to Armos Knights', 'and the key', 'the unlocking kid', 'keys for sale', 'unlock the fungus', 'key boy opens door again', 'a small key to Eastern Palace'),
              'Big Key (Eastern Palace)': (False, False, 'BigKey', 0x9D, 'A big key to Armos Knights', 'and the big key', 'the big-unlock kid', 'big key for sale', 'face key fungus', 'key boy opens chest again', 'a big key to Eastern Palace'),
              'Compass (Eastern Palace)': (False, True, 'Compass', 0x8D, 'Now you can find the Armos Knights!', 'and the compass', 'the magnetic kid', 'compass for sale', 'magnetic fungus', 'compass boy finds boss again', 'a compass to Eastern Palace'),
              'Map (Eastern Palace)': (False, True, 'Map', 0x7D, 'A tightly folded map rests here', 'and the map', 'cartography kid', 'map for sale', 'a map to shrooms', 'map boy navigates again', 'a map to Eastern Palace'),
              'Small Key (Desert Palace)': (False, False, 'SmallKey', 0xA3, 'A small key to the desert', 'and the key', 'the unlocking kid', 'keys for sale', 'unlock the fungus', 'key boy opens door again', 'a small key to Desert Palace'),
              'Big Key (Desert Palace)': (False, False, 'BigKey', 0x9C, 'A big key to the desert', 'and the big key', 'the big-unlock kid', 'big key for sale', 'face key fungus', 'key boy opens chest again', 'a big key to Desert Palace'),
              'Compass (Desert Palace)': (False, True, 'Compass', 0x8C, 'Now you can find Lanmolas!', 'and the compass', 'the magnetic kid', 'compass for sale', 'magnetic fungus', 'compass boy finds boss again', 'a compass to Desert Palace'),
              'Map (Desert Palace)': (False, True, 'Map', 0x7C, 'A tightly folded map rests here', 'and the map', 'cartography kid', 'map for sale', 'a map to shrooms', 'map boy navigates again', 'a map to Desert Palace'),
              'Small Key (Tower of Hera)': (False, False, 'SmallKey', 0xAA, 'A small key to Hera', 'and the key', 'the unlocking kid', 'keys for sale', 'unlock the fungus', 'key boy opens door again', 'a small key to Tower of Hera'),
              'Big Key (Tower of Hera)': (False, False, 'BigKey', 0x95, 'A big key to Hera', 'and the big key', 'the big-unlock kid', 'big key for sale', 'face key fungus', 'key boy opens chest again', 'a big key to Tower of Hera'),
              'Compass (Tower of Hera)': (False, True, 'Compass', 0x85, 'Now you can find Moldorm!', 'and the compass', 'the magnetic kid', 'compass for sale', 'magnetic fungus', 'compass boy finds boss again', 'a compass to Tower of Hera'),
              'Map (Tower of Hera)': (False, True, 'Map', 0x75, 'A tightly folded map rests here', 'and the map', 'cartography kid', 'map for sale', 'a map to shrooms', 'map boy navigates again', 'a map to Tower of Hera'),
              'Small Key (Hyrule Castle)': (False, False, 'SmallKey', 0xA0, 'A small key to the castle', 'and the key', 'the unlocking kid', 'keys for sale', 'unlock the fungus', 'key boy opens door again', 'a small key to Hyrule Castle'),
              'Big Key (Hyrule Castle)': (False, False, 'BigKey', 0x9F, 'A big key to the castle', 'and the big key', 'the big-unlock kid', 'big key for sale', 'face key fungus', 'key boy opens chest again', 'a big key to Hyrule Castle'),
              'Compass (Hyrule Castle)': (False, True, 'Compass', 0x8F, 'Now you can find no boss!', 'and the compass', 'the magnetic kid', 'compass for sale', 'magnetic fungus', 'compass boy finds boss again', 'a compass to Hyrule Castle'),
              'Map (Hyrule Castle)': (False, True, 'Map', 0x7F, 'A tightly folded map rests here', 'and the map', 'cartography kid', 'map for sale', 'a map to shrooms', 'map boy navigates again', 'a map to Hyrule Castle'),
              'Small Key (Agahnims Tower)': (False, False, 'SmallKey', 0xA4, 'A small key to Agahnim', 'and the key', 'the unlocking kid', 'keys for sale', 'unlock the fungus', 'key boy opens door again', 'a small key to Castle Tower'),
              # doors-specific items, baserom will not be able to understand these
              'Big Key (Agahnims Tower)': (False, False, 'BigKey', 0x9B, 'A big key to Agahnim', 'and the big key', 'the big-unlock kid', 'big key for sale', 'face key fungus', 'key boy opens chest again', 'a big key to Castle Tower'),
              'Compass (Agahnims Tower)': (False, True, 'Compass', 0x8B, 'Now you can find Aga1!', 'and the compass', 'the magnetic kid', 'compass for sale', 'magnetic fungus', 'compass boy finds null again', 'a compass to Castle Tower'),
              'Map (Agahnims Tower)': (False, True, 'Map', 0x7B, 'A tightly folded map rests here', 'and the map', 'cartography kid', 'map for sale', 'a map to shrooms', 'map boy navigates again', 'a map to Castle Tower'),
              # end of doors-specific items
              'Small Key (Palace of Darkness)': (False, False, 'SmallKey', 0xA6, 'A small key to darkness', 'and the key', 'the unlocking kid', 'keys for sale', 'unlock the fungus', 'key boy opens door again', 'a small key to Palace of Darkness'),
              'Big Key (Palace of Darkness)': (False, False, 'BigKey', 0x99, 'A big key to darkness', 'and the big key', 'the big-unlock kid', 'big key for sale', 'face key fungus', 'key boy opens chest again', 'a big key to Palace of Darkness'),
              'Compass (Palace of Darkness)': (False, True, 'Compass', 0x89, 'Now you can find Helmasaur King!', 'and the compass', 'the magnetic kid', 'compass for sale', 'magnetic fungus', 'compass boy finds boss again', 'a compass to Palace of Darkness'),
              'Map (Palace of Darkness)': (False, True, 'Map', 0x79, 'A tightly folded map rests here', 'and the map', 'cartography kid', 'map for sale', 'a map to shrooms', 'map boy navigates again', 'a map to Palace of Darkness'),
              'Small Key (Thieves Town)': (False, False, 'SmallKey', 0xAB, 'A small key to thievery', 'and the key', 'the unlocking kid', 'keys for sale', 'unlock the fungus', 'key boy opens door again', 'a small key to Thieves\' Town'),
              'Big Key (Thieves Town)': (False, False, 'BigKey', 0x94, 'A big key to thievery', 'and the big key', 'the big-unlock kid', 'big key for sale', 'face key fungus', 'key boy opens chest again', 'a big key to Thieves\' Town'),
              'Compass (Thieves Town)': (False, True, 'Compass', 0x84, 'Now you can find Blind!', 'and the compass', 'the magnetic kid', 'compass for sale', 'magnetic fungus', 'compass boy finds boss again', 'a compass to Thieves\' Town'),
              'Map (Thieves Town)': (False, True, 'Map', 0x74, 'A tightly folded map rests here', 'and the map', 'cartography kid', 'map for sale', 'a map to shrooms', 'map boy navigates again', 'a map to Thieves\' Town'),
              'Small Key (Skull Woods)': (False, False, 'SmallKey', 0xA8, 'A small key to the woods', 'and the key', 'the unlocking kid', 'keys for sale', 'unlock the fungus', 'key boy opens door again', 'a small key to Skull Woods'),
              'Big Key (Skull Woods)': (False, False, 'BigKey', 0x97, 'A big key to the woods', 'and the big key', 'the big-unlock kid', 'big key for sale', 'face key fungus', 'key boy opens chest again', 'a big key to Skull Woods'),
              'Compass (Skull Woods)': (False, True, 'Compass', 0x87, 'Now you can find Mothula!', 'and the compass', 'the magnetic kid', 'compass for sale', 'magnetic fungus', 'compass boy finds boss again', 'a compass to Skull Woods'),
              'Map (Skull Woods)': (False, True, 'Map', 0x77, 'A tightly folded map rests here', 'and the map', 'cartography kid', 'map for sale', 'a map to shrooms', 'map boy navigates again', 'a map to Skull Woods'),
              'Small Key (Swamp Palace)': (False, False, 'SmallKey', 0xA5, 'A small key to the swamp', 'and the key', 'the unlocking kid', 'keys for sale', 'unlock the fungus', 'key boy opens door again', 'a small key to Swamp Palace'),
              'Big Key (Swamp Palace)': (False, False, 'BigKey', 0x9A, 'A big key to the swamp', 'and the big key', 'the big-unlock kid', 'big key for sale', 'face key fungus', 'key boy opens chest again', 'a big key to Swamp Palace'),
              'Compass (Swamp Palace)': (False, True, 'Compass', 0x8A, 'Now you can find Arrghus!', 'and the compass', 'the magnetic kid', 'compass for sale', 'magnetic fungus', 'compass boy finds boss again', 'a compass to Swamp Palace'),
              'Map (Swamp Palace)': (False, True, 'Map', 0x7A, 'A tightly folded map rests here', 'and the map', 'cartography kid', 'map for sale', 'a map to shrooms', 'map boy navigates again', 'a map to Swamp Palace'),
              'Small Key (Ice Palace)': (False, False, 'SmallKey', 0xA9, 'A small key to the iceberg', 'and the key', 'the unlocking kid', 'keys for sale', 'unlock the fungus', 'key boy opens door again', 'a small key to Ice Palace'),
              'Big Key (Ice Palace)': (False, False, 'BigKey', 0x96, 'A big key to the iceberg', 'and the big key', 'the big-unlock kid', 'big key for sale', 'face key fungus', 'key boy opens chest again', 'a big key to Ice Palace'),
              'Compass (Ice Palace)': (False, True, 'Compass', 0x86, 'Now you can find Kholdstare!', 'and the compass', 'the magnetic kid', 'compass for sale', 'magnetic fungus', 'compass boy finds boss again', 'a compass to Ice Palace'),
              'Map (Ice Palace)': (False, True, 'Map', 0x76, 'A tightly folded map rests here', 'and the map', 'cartography kid', 'map for sale', 'a map to shrooms', 'map boy navigates again', 'a map to Ice Palace'),
              'Small Key (Misery Mire)': (False, False, 'SmallKey', 0xA7, 'A small key to the mire', 'and the key', 'the unlocking kid', 'keys for sale', 'unlock the fungus', 'key boy opens door again', 'a small key to Misery Mire'),
              'Big Key (Misery Mire)': (False, False, 'BigKey', 0x98, 'A big key to the mire', 'and the big key', 'the big-unlock kid', 'big key for sale', 'face key fungus', 'key boy opens chest again', 'a big key to Misery Mire'),
              'Compass (Misery Mire)': (False, True, 'Compass', 0x88, 'Now you can find Vitreous!', 'and the compass', 'the magnetic kid', 'compass for sale', 'magnetic fungus', 'compass boy finds boss again', 'a compass to Misery Mire'),
              'Map (Misery Mire)': (False, True, 'Map', 0x78, 'A tightly folded map rests here', 'and the map', 'cartography kid', 'map for sale', 'a map to shrooms', 'map boy navigates again', 'a map to Misery Mire'),
              'Small Key (Turtle Rock)': (False, False, 'SmallKey', 0xAC, 'A small key to the pipe maze', 'and the key', 'the unlocking kid', 'keys for sale', 'unlock the fungus', 'key boy opens door again', 'a small key to Turtle Rock'),
              'Big Key (Turtle Rock)': (False, False, 'BigKey', 0x93, 'A big key to the pipe maze', 'and the big key', 'the big-unlock kid', 'big key for sale', 'face key fungus', 'key boy opens chest again', 'a big key to Turtle Rock'),
              'Compass (Turtle Rock)': (False, True, 'Compass', 0x83, 'Now you can find Trinexx!', 'and the compass', 'the magnetic kid', 'compass for sale', 'magnetic fungus', 'compass boy finds boss again', 'a compass to Turtle Rock'),
              'Map (Turtle Rock)': (False, True, 'Map', 0x73, 'A tightly folded map rests here', 'and the map', 'cartography kid', 'map for sale', 'a map to shrooms', 'map boy navigates again', 'a map to Turtle Rock'),
              'Small Key (Ganons Tower)': (False, False, 'SmallKey', 0xAD, 'A small key to the evil tower', 'and the key', 'the unlocking kid', 'keys for sale', 'unlock the fungus', 'key boy opens door again', 'a small key to Ganon\'s Tower'),
              'Big Key (Ganons Tower)': (False, False, 'BigKey', 0x92, 'A big key to the evil tower', 'and the big key', 'the big-unlock kid', 'big key for sale', 'face key fungus', 'key boy opens chest again', 'a big key to Ganon\'s Tower'),
              'Compass (Ganons Tower)': (False, True, 'Compass', 0x82, 'Now you can find Agahnim!', 'and the compass', 'the magnetic kid', 'compass for sale', 'magnetic fungus', 'compass boy finds boss again', 'a compass to Ganon\'s Tower'),
              'Map (Ganons Tower)': (False, True, 'Map', 0x72, 'A tightly folded map rests here', 'and the map', 'cartography kid', 'map for sale', 'a map to shrooms', 'map boy navigates again', 'a map to Ganon\'s Tower'),
              'Small Key (Universal)': (False, True, None, 0xAF, 'A small key for any door', 'and the key', 'the unlocking kid', 'keys for sale', 'unlock the fungus', 'key boy opens door again', 'a small key'),
              'Nothing': (False, False, None, 0x5A, 'Some Hot Air', 'and the Nothing', 'the zen kid', 'outright theft', 'shroom theft', 'empty boy is bored again', 'nothing'),
              'Bee Trap': (False, False, None, 0xB0, 'We will sting your face a whole lot!', 'and the sting buddies', 'the beekeeper kid', 'insects for sale', 'shroom pollenation', 'bottle boy has mad bees again', 'Friendship'),
              'Red Potion': (False, False, None, 0x2E, 'Hearty red goop!', 'and the red goo', 'the liquid kid', 'potion for sale', 'free samples', 'bottle boy has red goo again', 'a red potion'),
              'Green Potion': (False, False, None, 0x2F, 'Refreshing green goop!', 'and the green goo', 'the liquid kid', 'potion for sale', 'free samples', 'bottle boy has green goo again', 'a green potion'),
              'Blue Potion': (False, False, None, 0x30, 'Delicious blue goop!', 'and the blue goo', 'the liquid kid', 'potion for sale', 'free samples', 'bottle boy has blue goo again', 'a blue potion'),
              'Bee': (False, False, None, 0x0E, 'I will sting your foes a few times', 'and the sting buddy', 'the beekeeper kid', 'insect for sale', 'shroom pollenation', 'bottle boy has mad bee again', 'a bee'),
              'Small Heart': (False, False, None, 0x42, 'Just a little\npiece of love!', 'and the heart', 'the life-giving kid', 'little love for sale', 'fungus for life', 'life boy feels some love again', 'a heart'),
              'Beat Agahnim 1': (True, False, 'Event', None, None, None, None, None, None, None, None),
              'Beat Agahnim 2': (True, False, 'Event', None, None, None, None, None, None, None, None),
              'Get Frog': (True, False, 'Event', None, None, None, None, None, None, None, None),
              'Return Smith': (True, False, 'Event', None, None, None, None, None, None, None, None),
              'Pick Up Purple Chest': (True, False, 'Event', None, None, None, None, None, None, None, None),
              'Open Floodgate': (True, False, 'Event', None, None, None, None, None, None, None, None),
              }

lookup_id_to_name = {data[3]: name for name, data in item_table.items()}

hint_blacklist = {"Triforce"}

item_name_groups = {"Bows": {"Bow", "Silver Arrows", "Silver Bow", "Progressive Bow (Alt)", "Progressive Bow"},
                    "Gloves": {"Power Glove", "Progressive Glove", "Titans Mitts"},
                    "Medallions": {"Ether", "Bombos", "Quake"}}
# generic groups, (Name, substring)
_simple_groups = {("Swords", "Sword"),

                  ("Small Keys", "Small Key"),
                  ("Big Keys", "Big Key"),
                  ("Compasses", "Compass"),
                  ("Maps", "Map"),

                  ("Bottles", "Bottle"),
                  ("Potions", "Potion"),
                  ("Rupees", "Rupee"),
                  ("Clocks", "Clock")
                  }
for basename, substring in _simple_groups:
    tempset = item_name_groups[basename] = set()
    for itemname in item_table:
        if substring in itemname:
            tempset.add(itemname)

del (_simple_groups)

progression_items = {name for name, data in item_table.items() if type(data[3]) == int and data[0]}
