from ..model import attributes, card_type

# TODO (visitor) they have random ineterst in 'affair'

# DI Douglas Moore
#
# Detective-Illuminate of the Suppression Bureau. A stoic, but weary, fellow. His dearest wish is to move to Chingford and grow roses. But the buggers won't let him retire.
di_douglas_moore = card_type("di_douglas_moore",
    attributes(interested_in_heart=3, interested_in_lantern=3, visitor=1, occupant=1, understands_greek=1),
)


# Dr Arun Peel
#
# Exile, riddlemonger, Thunderskin devotee. ('I'd rather say confidant.') Impeccably dressed, but always in dark clothing so the stains don't show. Dark the dressings too at his ankles and his wrists. ('I won't take a seat. It's kind of you to offer. It would be unkind of me to accept.')
dr_arun_peel = card_type("dr_arun_peel",
    attributes(moon=1, interested_in_moon=3, interested_in_moth=3, visitor=1, understands_aramaic=1, understands_vak=1, understands_sanskrit=1, occupant=1, understands_latin=1, understands_phrygian=1, understands_greek=1),
)


# Dr Ibn al-Adim
#
# 'The Aleppine': Historian, doctor, and above all, traveller. The good doctor has been associated with all but one of the libraries of the Watchman's Tree. He was even Secretary Nunciant of Hush House for a little while, but he has never been on good terms with the Suppression Bureau.
dr_ibn_al_adim = card_type("dr_ibn_al_adim",
    attributes(interested_in_rose=3, interested_in_scale=3, visitor=1, understands_aramaic=1, understands_phrygian=1, understands_greek=1, understands_sanskrit=1, occupant=1, understands_sabazine=1, understands_latin=1),
)


# Dr Yvette Southey
#
# Playwright, philologist, psychoanalyst: as happy with questions as with answers.
dr_yvette_southey = card_type("dr_yvette_southey",
    attributes(interested_in_moon=3, interested_in_winter=3, visitor=1, understands_ericapaean=1, occupant=1, understands_greek=1, understands_kernewek_henavek=1, understands_latin=1),
)


# Fr. Stanislav John Schaller
#
# Priest, diplomat, gardener: a soft-voiced man with a very steady gaze.
fr_stanislav_john_schaller = card_type("fr_stanislav_john_schaller",
    attributes(interested_in_heart=3, interested_in_nectar=3, visitor=1, understands_phrygian=1, understands_cracktrack=1, understands_sanskrit=1, understands_fucine=1, occupant=1, understands_greek=1, understands_latin=1),
)


# Julian Coseley
#
# Magus, Winter-long, controversial philosopher. For an immortal exalted by an Hour of Silence, especially one who might be dead, he has had a great deal to say for himself over the years.
julian_coseley = card_type("julian_coseley",
    attributes(interested_in_moon=7, interested_in_winter=7, visitor=1, understands_aramaic=1, understands_phrygian=1, understands_ericapaean=1, from_numa=1, understands_greek=1, understands_latin=1),
)


# Lalla Chaima
#
# Huntress, goumier, occasional Bureau consultant. When it can't be killed, and it really needs killing, Chaima's the one they turn to.
lalla_chaima = card_type("lalla_chaima",
    attributes(edge=1, interested_in_edge=3, interested_in_rose=3, visitor=1, understands_aramaic=1, understands_cracktrack=1, occupant=1, understands_greek=1),
)


# MCO Constance Lee
#
# Connie has risen swiftly in the Suppression Bureau, to the exalted rank of Constable-Oculate Minor. Don't get in her way.
mco_constance_lee = card_type("mco_constance_lee",
    attributes(moon=1, interested_in_moon=3, interested_in_sky=3, visitor=1, understands_aramaic=1, occupant=1, understands_greek=1, understands_killasimi=1, understands_latin=1),
)


# Mr Ehsan Fekri
#
# Formerly; Ehsan was a healer; he was not human; he was Secretary Salvant of Hush House. But not all at the same time. Fussy, kind, famously foul to look upon.
mr_ehsan_fekri = card_type("mr_ehsan_fekri",
    attributes(interested_in_heart=3, interested_in_sky=3, visitor=1, understands_aramaic=1, occupant=1, understands_greek=1, understands_deep_mandaic=1),
)


# Mr Fraser Strathcoyne
#
# Philanthropist, collector, former Librarian. A complicated man, but not a cruel one.
mr_fraser_strathcoyne = card_type("mr_fraser_strathcoyne",
    attributes(interested_in_lantern=1, interested_in_scale=1, inspired=1, visitor=1, sympathy_carapace=1, understands_ramsund=1, occupant=1),
)


# Mr Peter Agdistis
#
# Musician, mystic, impresario. Agdistis was a dancer once. One cannot see him without knowing it. The wound in his thigh keeps him from the stage; but his every movement still has the cadence of a prayer.
mr_peter_agdistis = card_type("mr_peter_agdistis",
    attributes(interested_in_heart=3, interested_in_sky=3, visitor=1, understands_aramaic=1, understands_fucine=1, occupant=1, understands_greek=1, understands_phrygian=1),
)


# Mr Zachary Wakefield
#
# Marksman, detective, renegade. He has always been a quiet man, but since he left the Suppression Bureau, he has grown even quieter, and terribly still - except for his fingers and for his eyes, always in restless motion.
mr_zachary_wakefield = card_type("mr_zachary_wakefield",
    attributes(interested_in_knock=1, interested_in_winter=1, visitor=1, understands_phrygian=1, understands_fucine=1, occupant=1, understands_greek=1, understands_latin=1, understands_killasimi=1),
)


# Ms Azita Bukhara
#
# Businesswoman, chess-master, initiate of the scarred Hour sometimes called the Colonel.
ms_azita_bukhara = card_type("ms_azita_bukhara",
    attributes(edge=1, interested_in_edge=3, interested_in_sky=3, visitor=1, understands_aramaic=1, understands_phrygian=1, occupant=1, understands_latin=1, understands_deep_mandaic=1),
)


# Professor Rowena Hengerst
#
# For many years, under many names, Rowena has done, learnt, or eaten many things she really shouldn't have. But for many years, under many names, she's served as the protectress of Hush House.
professor_rowena_hengerst = card_type("professor_rowena_hengerst",
    attributes(interested_in_grail=7, interested_in_winter=7, visitor=1, understands_phrygian=1, from_numa=1, understands_greek=1, understands_kernewek_henavek=1),
)
