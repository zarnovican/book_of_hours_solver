from frozendict import frozendict
import json
from pprint import pprint

from boh import room, station
from boh.item import *
from boh.model import season
from boh.solver import solver
from boh.state import state
from streamlit_utils import app_state_from_boh, minimize_app_state

s = state()
r = solver(state=s)

s.skill_cap({
    skill.anbary_and_lapidary:                  8,
    skill.applebright_euphonies:                5,
    skill.auroral_contemplations:               9,
    skill.bells_and_brazieries:                 3,
    skill.coil_and_chasm:                       9,
    skill.cracktrack:                           1,
    skill.deep_mandaic:                         1,
    skill.desires_and_dissolutions:             4,
    skill.disciplines_of_the_hammer:            7,
    skill.disciplines_of_the_scar:              3,
    skill.door_and_wall:                        3,
    skill.drums_and_dances:                     8,
    skill.edicts_inviolable:                    7,
    skill.edicts_liminal:                       5,
    skill.edicts_martial:                       9,
    skill.ericapaean:                           1,
    skill.fucine:                               2,
    skill.furs_and_feathers:                    2,
    skill.glassblowing_and_vesselcrafting:      6,
    skill.glaziery_and_lightsmithing:           4,
    skill.herbs_and_infusions:                  6,
    skill.hill_and_hollow:                      2,
    skill.horns_and_ivories:                    4,
    skill.hyksos:                               2,
    skill.inks_of_containment:                  8,
    skill.inks_of_power:                        9,
    skill.inks_of_revelation:                   7,
    skill.insects_and_nectars:                  9,
    skill.kernewek_henavek:                     3,
    skill.killasimi:                            2,
    skill.leaves_and_thorns:                    9,
    skill.lockworks_and_clockworks:             7,
    skill.maggephene_mysteries:                 4,
    skill.meniscate_reflections:                5,
    skill.orchids_and_narcotics:                7,
    skill.ouranoscopy:                          7,
    skill.path_and_pilgrim:                     8,
    skill.pearl_and_tide:                       5,
    skill.pentiments_and_precursors:            3,
    skill.preliminal_meter:                     8,
    skill.purifications_and_exaltations:        1,
    skill.putrefactions_and_calcinations:       6,
    skill.pyroglyphics:                         2,
    skill.quenchings_and_quellings:             4,
    skill.ragged_crossroads:                    9,
    skill.ramsund:                              1,
    skill.resurgences_and_emergences:           6,
    skill.rhyme_and_remembrance:                3,
    skill.rites_of_the_roots:                   9,
    skill.sabazine:                             2,
    skill.sacra_limiae:                         4,
    skill.sacra_solis_invicti:                  6,
    skill.sand_stories:                         6,
    skill.sea_stories:                          2,
    skill.serpents_and_venoms:                  7,
    skill.sharps:                               5,
    skill.sickle_and_eclipse:                   4,
    skill.sights_and_sensations:                8,
    skill.sky_stories:                          8,
    skill.snow_stories:                         2,
    skill.solutions_and_separations:            8,
    skill.spices_and_savours:                   5,
    skill.stitching_and_binding:                6,
    skill.stone_stories:                        8,
    skill.strings_and_songs:                    7,
    skill.surgeries_and_exsanguinations:        3,
    skill.the_great_signs_and_the_great_scars:  5,
    skill.transformations_and_liberations:      9,
    skill.tridesma_hiera:                       5,
    skill.vak:                                  1,
    skill.watchmans_paradoxes:                  7,
    skill.weaving_and_knotworking:              1,
    skill.wolf_stories:                         5,
})

# prologue
# * pick fet + phost
s.inventory_add(
    journal.a_drowned_book_fet_phost,
    soul.fet,
    soul.health,
    soul.phost,
)
s.unlock(room.brancrug_village)
s.unlock_station(station.the_rectory)

# spring1
s.new_day(season=season.spring)
s.unlock_station(station.the_sweet_bones)
s.unlock(room.cucurbit_bridge)
s.unlock(room.keepers_lodge)
s.inventory_remove(
    thing.hush_house_key,
)

# spring2
s.new_day()
s.unlock(room.watchmans_tower_gatehouse)
s.inventory_remove(
    journal.a_drowned_book_fet_phost,
)
s.inventory_add(
    journal.serpentskin_journal,
    soul.fet,
    soul.trist,
)
s.unlock(room.watchmans_tower_first_floor)
s.unlock(room.st_brandans_cloister)
s.catalogue(
    codex.the_ceaseless_tantra,     # Watchman's Tower: First Floor
)
s.unlock(room.crowcross_sands)

# spring3
s.new_day()
s.unlock(room.long_tower_solomons_study)
s.inventory_remove(
    journal.serpentskin_journal,
)
s.inventory_add(
    journal.serpentskin_journal_mastered,
    lesson.inks_of_revelation,
    lesson.inks_of_revelation,
    lesson.inks_of_revelation,
    lesson.path_and_pilgrim,
    thing.hush_house_key,
)
s.catalogue(
    codex.old_coppernose_and_the_softer_metal,  # Watchman's Tower: First Floor
)
s.unlock(room.watchmans_tower_observatory)
s.master(codex.the_ceaseless_tantra)
s.commit(skill.weaving_and_knotworking, wisdom="the_bosk")

# spring4
s.new_day()
s.inventory_remove(
    liquid.yewgall_ink,
)
s.unlock(room.entrance_hall)
s.unlock(room.physic_garden)
s.catalogue(
    codex.the_manner_in_which_the_alchemist_was_spared, # Watchman's Tower: First Floor
)
s.unlock(room.long_tower_solomons_quarters)

# spring5
s.new_day()
s.catalogue(
    scroll.the_incandescent_tantra,     # Watchman's Tower: First Floor
    codex.a_shape_in_smoke,             # Watchman's Tower: First Floor
    codex.prophecies_of_glory,          # Watchman's Tower: First Floor
)
s.inventory_remove(
    beverage.dandelion_wine_glass,
    beverage.mist_kissed_water_glass,
    beverage.roscraggan_whisky_glass,
    candle.widows_candle,
)
s.brew(leaf.ch_second_flush_assam_packet)
s.unlock(room.infirmary)
s.unlock(room.scent_garden)
s.unlock(room.grand_ascent_ground_floor)

# spring6
s.new_day()
s.brew(material.dawnlion_coffee_packet)
s.catalogue(
    codex.fekris_herbary,               # Watchman's Tower: First Floor
    codex.an_impertinent_vitulation,    # Watchman's Tower: First Floor
    codex.the_republic_of_teeth,        # Watchman's Tower: First Floor
    codex.musgraves_sketches,           # Long Tower: Solomon's Study
)
s.unlock(room.reading_room)
s.inventory_remove(
    beverage.trn_limited_drinking_cocoa_cup,
)

# summer1
s.new_day(season=season.summer)
s.unlock(room.servants_hall)
s.catalogue(
    codex.the_temptations_of_architecture,  # Long Tower: Solomon's Study
    codex.letters_from_a_fugitive,          # Long Tower: Solomon's Study
    codex.the_carmine_petal_revised,        # Watchman's Tower: First Floor
    codex.the_humours_of_a_gentleman,       # Long Tower: Solomon's Study
)
s.inventory_remove(
    beverage.veiled_goddess_lapsang_souchong_cup,
    candle.honeyscar_scented_candle,
    liquid.houndsgall,
)
s.unlock(room.kitchen)
s.master(codex.the_republic_of_teeth)
s.master(codex.letters_from_a_fugitive)
s.inventory_add(
    skill.cracktrack,
)
s.commit(skill.cracktrack, wisdom="preservation")

# summer2
s.new_day()
s.upgrade(skill.path_and_pilgrim, using=lesson.path_and_pilgrim)
s.master(codex.the_humours_of_a_gentleman)
s.catalogue(
    codex.three_flowers_hath_the_tree,      # Long Tower: Solomon's Study
    reel_of_film.colours_in_the_liver,      # Long Tower: Solomon's Study
)
s.unlock(room.grand_ascent_first_floor)

# summer3
s.new_day()
s.catalogue(
    codex.the_locksmiths_dream_a_light_through_the_keyhole, # Long Tower: Solomon's Study
    phonograph_record.recordings_from_the_althiban_abyss,   # Long Tower: Solomon's Study
    codex.the_encircling_tantra,                            # Watchman's Tower: First Floor
)
s.master(codex.the_locksmiths_dream_a_light_through_the_keyhole)
s.commit(skill.purifications_and_exaltations, wisdom="illumination")
s.master(codex.prophecies_of_glory)
s.master(codex.three_flowers_hath_the_tree)
s.upgrade(skill.sky_stories, using=lesson.watchmans_paradoxes)
s.unlock(room.patients_lounge)

# summer4
s.new_day()
s.catalogue(
    codex.the_chandlers_wish,                   # Long Tower: Solomon's Study
    codex.the_twelve_letters_on_consequence,    # Long Tower: Solomon's Study
    codex.warming_draughts_to_uplift_the_heart, # Long Tower: Solomon's Study
)
s.master(codex.the_encircling_tantra)
s.master(codex.travelling_at_night_vol_2)
s.unlock(room.motley_tower_illopolys_nook)
s.master(codex.travelling_at_night_vol_1)
s.inventory_add(
    beverage.roscraggan_whisky_bottle,
)

# summer5
s.new_day()
s.catalogue(
    codex.it_is_written,                        # Long Tower: Solomon's Study
    codex.opus_magnum_caeruleum,                # Watchman's Tower: First Floor
    codex.in_the_malleary,                      # Watchman's Tower: First Floor
)
s.inventory_add(
    liquid.yewgall_ink,
)
s.master(codex.warming_draughts_to_uplift_the_heart)
s.upgrade(skill.herbs_and_infusions, using=lesson.herbs_and_infusions)
s.unlock(room.westcott_room)
s.master(codex.fekris_herbary)
s.unlock(room.practic_garden)
s.upgrade(skill.herbs_and_infusions, using=lesson.herbs_and_infusions)

# summer6
s.new_day()
s.inventory_remove(
    beverage.trn_limited_drinking_cocoa_cup,
)
s.catalogue(
    codex.chione_at_abydos,                     # Long Tower: Solomon's Study
)
s.unlock(room.grand_ascent_second_floor)
s.master(codex.musgraves_sketches)
s.upgrade(skill.sights_and_sensations, using=lesson.sights_and_sensations)
s.unlock(room.motley_tower_dispensary)

# autumn1
s.new_day(season=season.autumn)
s.catalogue(
    codex.a_journey_to_the_grove,               # Long Tower: Solomon's Quarters
    codex.the_moons_egg,                        # Long Tower: Solomon's Study
)
s.inventory_remove(
    beverage.ch_second_flush_assam_cup,
    liquid.honey,
)
s.upgrade(skill.sights_and_sensations, using=lesson.sights_and_sensations)
s.master(codex.in_the_malleary)
s.master(codex.chione_at_abydos)
s.unlock(room.motley_tower_regensburg_room)
s.inventory_add(
    skill.fucine,
)

###############################################################################################
inventory_addition = (
    beverage.roscraggan_whisky_bottle,
    beverage.ch_second_flush_assam_cup,
    beverage.dawnlion_coffee_cup,
    beverage.dawnlion_coffee_cup,
)
inventory_removal = (
    beverage.dandelion_wine_glass,
    beverage.mist_kissed_water_glass,
    beverage.roscraggan_whisky_glass,
    candle.widows_candle,
    beverage.trn_limited_drinking_cocoa_cup,
    beverage.veiled_goddess_lapsang_souchong_cup,
    candle.honeyscar_scented_candle,
    liquid.houndsgall,
    beverage.trn_limited_drinking_cocoa_cup,
    liquid.honey,
)
json.dump(minimize_app_state(app_state_from_boh(s, inventory_addition, inventory_removal)), open("sample_early.json", "w"), indent=2)

# autumn2
s.new_day()
s.catalogue(
    codex.my_deeds_my_powers_my_achievements_and_the_injustices_perpetrated_against_me,
    codex.the_elations_of_limentinus,           # Long Tower: Solomon's Study
    codex.the_dream_of_the_conspiracy_of_the_lower_skies,
)
s.inventory_remove(
    liquid.catwink,
    candle.widows_candle,
)
s.inventory_add(
    liquid.paint_bosk_green,
)
s.unlock(room.grand_ascent_third_floor)
s.master(codex.the_moons_egg)
s.master(codex.the_twelve_letters_on_consequence)
s.unlock(room.severn_chamber)

# autumn3
s.new_day()
s.catalogue(
    codex.ambrosial,
    codex.five_creations,
    codex.the_book_of_the_centipede,
    codex.the_six_letters_on_necessity,
)
s.inventory_remove(
    liquid.ashartine,
)
s.master(codex.opus_magnum_caeruleum)
s.upgrade(skill.pyroglyphics, using=lesson.inks_of_revelation)
s.unlock(room.map_room)
s.commit(skill.pyroglyphics, wisdom="illumination")
s.master(codex.the_book_of_the_centipede)

# autumn4
s.new_day()
s.catalogue(
    codex.the_shadow_in_the_stair,
    codex.evas_treasury,
    codex.the_amalgam_of_the_red_rose,
)
s.master(codex.the_six_letters_on_necessity)
s.master(codex.the_temptations_of_architecture)
s.master(codex.the_elations_of_limentinus)
s.upgrade(skill.transformations_and_liberations, using=lesson.inks_of_revelation)
s.upgrade(skill.transformations_and_liberations, using=lesson.pyroglyphics)
s.master(codex.the_shadow_in_the_stair)
s.unlock(room.atrium)
s.upgrade(skill.the_great_signs_and_the_great_scars, using=lesson.door_and_wall)

# autumn5
s.new_day()
s.catalogue(
    codex.exorcism_for_girls,
    codex.nyns_cages_avignon_text,
    codex.on_resonance,
    codex.apollo_and_marsyas,
    codex.oblations_in_iron,
    phonograph_record.an_investigation_of_a_foundered_country,
    codex.the_intimations_of_skin,
)
s.master(codex.ambrosial)
s.unlock(room.examination_room)
s.master(codex.apollo_and_marsyas)
s.inventory_remove(
    candle.aglaophotis_scented_candle,
)
s.unlock(room.violet_chamber)

# autumn6
s.new_day()
s.catalogue(
    codex.snare_of_the_tree_collected_proverbs_of_aunt_mopsy,
    scroll.the_leonine_tantra,
)
s.inventory_remove(
    beverage.ch_second_flush_assam_cup,
    liquid.perinculate,
    beverage.dandelion_wine_glass,
)
s.master(codex.oblations_in_iron)
s.master(phonograph_record.an_investigation_of_a_foundered_country)
s.master(scroll.the_leonine_tantra)
s.upgrade(skill.edicts_martial, using=lesson.edicts_martial)
s.unlock(room.pantry)
s.master(codex.it_is_written)
s.upgrade(skill.hill_and_hollow, using=lesson.inks_of_power)
s.commit(skill.hill_and_hollow, wisdom="preservation")

# winter1
s.new_day(season=season.winter)
s.catalogue(
    codex.the_debate_of_seven_cups,
    codex.advice_on_containment,
    codex.the_devoured_tantra,
    codex.the_victory_of_crowns,
    codex.inaam_kapigiginlupir_garkie_cryppys,
    codex.twenty_six_enticements_seven_torments,
    codex.an_exorcists_field_manual,
    codex.cucurbit_prisoner_records_1928,
)
s.malady(soul.health)
s.master(codex.the_amalgam_of_the_red_rose)
s.upgrade(skill.edicts_martial, using=lesson.meniscate_reflections)
s.master(codex.advice_on_containment)
s.malady(soul.health)
s.master(codex.the_victory_of_crowns)
s.unlock(room.mazarine_room)
s.upgrade(skill.transformations_and_liberations, using=lesson.spices_and_savours)

# winter2
s.new_day()
s.catalogue(
    codex.the_radical_measure,
    codex.on_the_winding_stair,
    codex.the_locksmiths_dream_stolen_reflections,
    codex.perugian_diaries,
    codex.the_ascendant,
    codex.what_does_not_bark,
    codex.the_bee_keepers_ends,
    codex.journal_of_thomas_dewulf,
    codex.on_what_is_contained_by_silver,
    codex.the_barrowchilds_elegies,
)
s.inventory_remove(
    beverage.ch_second_flush_assam_cup,
    candle.small_candlestick,
)
s.master(codex.an_exorcists_field_manual)
s.upgrade(skill.edicts_martial, using=lesson.edicts_martial)
s.unlock(room.nave_of_the_abbey_church)
s.master(codex.the_devoured_tantra)
s.master(codex.perugian_diaries)
s.master(codex.evas_treasury)
s.master(codex.journal_of_thomas_dewulf)
s.unlock(room.fludd_gallery)

# winter3
s.new_day()
s.upgrade(skill.strings_and_songs, using=lesson.anbary_and_lapidary)
s.master(codex.the_locksmiths_dream_stolen_reflections)
s.inventory_remove(
    beverage.armagnac_dys_glass,
    candle.widows_candle,
    candle.small_candlestick,
)
s.catalogue(
    codex.collected_hush_house_lectures,
    scroll.the_fire_circle_tantra,
    codex.codex_acephali,
    codex.two_wombs_one_heart,
    codex.to_a_pale_lady,
    codex.the_mirror_of_melancthe,
    codex.the_gospel_of_zacchaeus,
)
s.upgrade(skill.strings_and_songs, using=lesson.watchmans_paradoxes)
s.master(codex.what_does_not_bark)
s.unlock(room.well)
s.master(codex.on_resonance)
s.master(codex.on_what_is_contained_by_silver)
s.master(codex.collected_hush_house_lectures)
s.unlock(room.glorious_stair)

# winter4
s.new_day()
s.master(codex.the_barrowchilds_elegies)
s.upgrade(skill.inks_of_containment, using=lesson.rhyme_and_remembrance)
s.upgrade(skill.strings_and_songs, using=lesson.glassblowing_and_vesselcrafting)
s.unlock(room.pale_chamber)
s.master(codex.old_coppernose_and_the_softer_metal)
s.upgrade(skill.strings_and_songs, using=lesson.bells_and_brazieries)
s.inventory_remove(
    beverage.ch_second_flush_assam_cup,
)
#s.brew(material.trn_limited_drinking_cocoa_packet)
s.master(codex.exorcism_for_girls)
s.upgrade(skill.edicts_martial, using=lesson.sickle_and_eclipse)
s.inventory_add(
    material.gervinite,
)
s.master(scroll.the_incandescent_tantra)
s.master(codex.an_impertinent_vitulation)
s.unlock(room.librarians_quarters)

# winter5
s.new_day()
s.upgrade(skill.strings_and_songs, using=lesson.bells_and_brazieries)
s.catalogue(
    codex.the_sea_does_not_regret,
    codex.exercises_in_the_continuity_of_self,
    codex.deaths_and_their_evasions,
    codex.seven_faces_of_icarus,
    codex.enchiridion_tragularis,
    codex.the_iron_book,
    codex.cardeas_delights,
)
s.inventory_add(
    flower.blue_crown,
    device.pale_mommet,
)
s.inventory_remove(
    candle.chalice_candle,
    beverage.trn_limited_drinking_cocoa_cup,
    liquid.catwink,
)
s.master(scroll.the_fire_circle_tantra)
s.master(codex.exercises_in_the_continuity_of_self)
s.master(codex.seven_faces_of_icarus)
s.upgrade(skill.inks_of_containment, using=lesson.rhyme_and_remembrance)
s.upgrade(skill.fucine, using=lesson.solutions_and_separations)
s.commit(skill.fucine, wisdom="ithastry")
s.upgrade(skill.the_great_signs_and_the_great_scars, using=lesson.leaves_and_thorns)
s.unlock(room.duelling_hall)

# winter6
s.new_day()
s.unlock(room.vestibulum_transitus)
s.upgrade(skill.transformations_and_liberations, using=lesson.transformations_and_liberations)
s.unlock_station(station.mr_and_mrs_kille)
s.catalogue(
    codex.the_ivory_book,
    codex.the_radical_measure_glossed,
)
s.inventory_remove(
    beverage.schloss_jannings_glass,
)
s.master(codex.the_sea_does_not_regret)
s.upgrade(skill.inks_of_containment, using=lesson.rhyme_and_remembrance)
s.inventory_add(
    flower.blue_crown,
)
s.upgrade(skill.path_and_pilgrim, using=lesson.pearl_and_tide)
s.master(reel_of_film.colours_in_the_liver)
s.unlock(room.servants_quarters_south)

# spring1
s.new_day(season=season.spring)
s.catalogue(
    codex.key_of_night,
    codex.the_orchid_transfigurations_a_feast,
    codex.a_seventh_voice,
)
s.inventory_remove(
    candle.watchful_candle,
    beverage.dawnlion_coffee_cup,
    candle.widows_candle,
)
s.master(codex.to_a_pale_lady)
s.upgrade(skill.edicts_martial, using=lesson.pearl_and_tide)
s.master(codex.the_mirror_of_melancthe)
s.upgrade(skill.furs_and_feathers, using=lesson.sights_and_sensations)
s.commit(skill.furs_and_feathers, wisdom="the_bosk")
s.upgrade(skill.path_and_pilgrim, using=lesson.pearl_and_tide)
s.unlock(room.windlit_gallery)
s.upgrade(skill.inks_of_containment, using=lesson.sights_and_sensations)
s.master(codex.key_of_night)
s.unlock(room.well_descent)

# spring2
s.new_day()
s.inventory_remove(
    candle.tall_candlestick,
    candle.small_candlestick,
)
s.master(codex.the_orchid_transfigurations_a_feast)
s.master(codex.a_seventh_voice)
s.upgrade(skill.surgeries_and_exsanguinations, using=lesson.preliminal_meter)
s.unlock(room.radiant_stair)
s.master(codex.the_radical_measure_glossed)
s.upgrade(skill.surgeries_and_exsanguinations, using=lesson.preliminal_meter)
s.catalogue(
    codex.a_light_in_the_inkwell,
    codex.those_indignities_perpetrated_by_the_deceitful_fraternity_of_obliviates,
    codex.de_motu_corporum_vetitorum,
    phonograph_record.a_tower_falls,
)
s.commit(skill.surgeries_and_exsanguinations, wisdom="preservation")
s.master(codex.the_ivory_book)
s.upgrade(skill.quenchings_and_quellings, using=lesson.quenchings_and_quellings)
s.unlock(room.foundry)

# spring3
s.new_day()
s.upgrade(skill.path_and_pilgrim, using=lesson.preliminal_meter)
s.brew(material.dawnlion_coffee_packet)
s.master(codex.those_indignities_perpetrated_by_the_deceitful_fraternity_of_obliviates)
s.unlock(room.hall_of_division)
s.catalogue(
    phonograph_record.lake_fucino_recordings,
    codex.isaac_of_karths_history_of_the_shadowless_kings,
    phonograph_record.velletri_interviews,
    codex.unhatched_hymns,
    codex.the_black_book_of_brittany,
    codex.nyns_cages_bruges_text,
    codex.commandments_for_the_preservation_of_all_that_exists,
)
s.inventory_remove(
    candle.bedside_candleholder,
)
s.inventory_add(
    codex.the_queens_of_the_rivers,
)
s.upgrade(skill.transformations_and_liberations, using=lesson.transformations_and_liberations)
s.unlock(room.chapter_house)
s.master(codex.the_queens_of_the_rivers)
s.master(phonograph_record.velletri_interviews)

# spring4
s.new_day()
s.upgrade(skill.strings_and_songs, using=lesson.edicts_inviolable)
s.inventory_remove(
    beverage.dawnlion_coffee_cup,
    candle.tall_candlestick,
)
s.unlock(room.chancel_of_the_abbey_church)
s.upgrade(skill.path_and_pilgrim, using=lesson.path_and_pilgrim)
s.master(codex.the_intimations_of_skin)
s.upgrade(skill.the_great_signs_and_the_great_scars, using=lesson.desires_and_dissolutions)
s.upgrade(skill.the_great_signs_and_the_great_scars, using=lesson.desires_and_dissolutions)
s.catalogue(
    codex.the_alloy_of_the_white_rose,
)
s.master(codex.a_shape_in_smoke)
s.unlock(room.church_tower)

# spring5
s.new_day()
s.unlock(room.solarium)
s.catalogue(
    codex.ud_rocashaas,
    codex.the_vinzant_inscriptions,
    codex.the_book_of_masks,
    codex.the_white_book_of_brittany,
    codex.a_second_glory,
    codex.an_echo_of_silence,
    codex.annals_of_st_brandans,
    codex.the_burning_woman,
    codex.the_high_mysteries_of_the_innermost_chamber_of_our_church_solar,
    codex.the_world_does_not_weep,
    codex.against_vitruvius,
    codex.book_of_true_blood,
    codex.gospel_of_nicodemus,
    codex.the_red_book_of_brittany,
    codex.medusas_lament,
    codex.the_winds_ruin,
    codex.the_origins_of_hours,
    codex.a_descent_of_the_shell,
)
s.inventory_remove(
    beverage.dawnlion_coffee_cup,
    device.pale_mommet,
    beverage.trn_limited_drinking_cocoa_cup,
)
s.brew(material.dawnlion_coffee_packet)
s.master(codex.annals_of_st_brandans)
s.upgrade(skill.ragged_crossroads, using=lesson.inks_of_containment)
s.unlock(room.kitchen_garden)
s.master(codex.against_vitruvius)

# spring6
s.new_day()
s.catalogue(
    codex.the_scar_in_the_sky,
    codex.against_the_sisterhood_of_the_knot_and_the_foulness_of_their_depraved_customs,
    codex.letters_to_my_successor,
)
s.upgrade(skill.transformations_and_liberations, using=lesson.pyroglyphics)
s.master(codex.the_winds_ruin)
s.upgrade(skill.leaves_and_thorns, using=lesson.applebright_euphonies)
s.master(codex.gospel_of_nicodemus)
s.master(codex.the_bee_keepers_ends)
s.unlock(room.night_gallery)
s.upgrade(skill.leaves_and_thorns, using=lesson.insects_and_nectars)
s.upgrade(skill.inks_of_revelation, using=lesson.pyroglyphics)
s.unlock(room.stair_tenebrous)
s.inventory_remove(
    beverage.ch_second_flush_assam_cup,
)
s.master(codex.de_motu_corporum_vetitorum)
s.master(codex.codex_acephali)
s.upgrade(skill.quenchings_and_quellings, using=lesson.snow_stories)
s.upgrade(skill.snow_stories, using=lesson.ouranoscopy)
s.inventory_add(
    leaf.vase_of_gorse,
)

# summer1
s.new_day(season=season.summer)
s.inventory_remove(
    beverage.strathcoyne_whisky_glass,
)
s.upgrade(skill.edicts_martial, using=lesson.ouranoscopy)
s.master(phonograph_record.lake_fucino_recordings)
s.upgrade(skill.quenchings_and_quellings, using=lesson.snow_stories)
s.catalogue(
    phonograph_record.a_tower_rises,
    codex.from_history_to_eternity,
)
s.commit(skill.quenchings_and_quellings, wisdom="preservation")
s.upgrade(skill.drums_and_dances, using=lesson.drums_and_dances)
s.master(codex.the_vinzant_inscriptions)
s.master(codex.cardeas_delights)
s.unlock(room.deep_well_descent)
s.upgrade(skill.solutions_and_separations, using=lesson.transformations_and_liberations)
s.upgrade(skill.leaves_and_thorns, using=lesson.the_great_signs_and_the_great_scars)
s.inventory_add(
    flower.agave_aeterna,
    material.beeswax,
)
s.master(codex.against_the_sisterhood_of_the_knot_and_the_foulness_of_their_depraved_customs)
s.master(codex.letters_to_my_successor)

# summer2
s.new_day()
s.inventory_add(
    skill.ericapaean,
    flower.fragrant_chalice,
    liquid.cuckoo_honey,
    liquid.honey,
)
s.commit(skill.ericapaean, wisdom="hushery")
s.commit(skill.snow_stories, wisdom="hushery")
s.upgrade(skill.inks_of_revelation, using=lesson.inks_of_revelation)
s.inventory_remove(
    beverage.armagnac_dys_glass,
    sustenance.soft_amber_pumpkin,
)
s.upgrade(skill.path_and_pilgrim, using=lesson.sky_stories)
s.upgrade(skill.leaves_and_thorns, using=lesson.the_great_signs_and_the_great_scars)
s.unlock(room.sacred_spring)
s.master(codex.a_light_in_the_inkwell)
s.upgrade(skill.solutions_and_separations, using=lesson.inks_of_revelation)
s.master(codex.the_radical_measure)
s.unlock_station(station.the_smithy)
s.upgrade(skill.solutions_and_separations, using=lesson.inks_of_revelation)

###############################################################################################
inventory_addition += (
    liquid.paint_bosk_green,
    material.gervinite,
    flower.blue_crown,
    device.pale_mommet,
    flower.blue_crown,
    leaf.vase_of_gorse,
    flower.agave_aeterna,
    material.beeswax,
    flower.fragrant_chalice,
    liquid.cuckoo_honey,
    liquid.honey,
)
inventory_removal += (
    liquid.catwink,
    candle.widows_candle,
    liquid.ashartine,
    candle.aglaophotis_scented_candle,
    beverage.ch_second_flush_assam_cup,
    liquid.perinculate,
    beverage.dandelion_wine_glass,
    beverage.ch_second_flush_assam_cup,
    candle.small_candlestick,
    beverage.armagnac_dys_glass,
    candle.widows_candle,
    candle.small_candlestick,
    beverage.ch_second_flush_assam_cup,
    candle.chalice_candle,
    beverage.trn_limited_drinking_cocoa_cup,
    liquid.catwink,
    beverage.schloss_jannings_glass,
    candle.tall_candlestick,
    candle.small_candlestick,
    candle.bedside_candleholder,
    beverage.dawnlion_coffee_cup,
    candle.tall_candlestick,
    beverage.armagnac_dys_glass,
    sustenance.soft_amber_pumpkin,
)
json.dump(minimize_app_state(app_state_from_boh(s, inventory_addition, inventory_removal)), open("sample_mid.json", "w"), indent=2)

# summer3
s.new_day()
s.brew(material.trn_limited_drinking_cocoa_packet)
s.inventory_remove(
    beverage.thirzas_cordials,
    liquid.cuckoo_honey,
    beverage.trn_limited_drinking_cocoa_cup,
)
s.upgrade(skill.path_and_pilgrim, using=lesson.preliminal_meter)
s.unlock(room.wine_cellar)
s.upgrade(skill.solutions_and_separations, using=lesson.preliminal_meter)
s.master(codex.snare_of_the_tree_collected_proverbs_of_aunt_mopsy)
s.upgrade(skill.leaves_and_thorns, using=lesson.applebright_euphonies)
s.unlock(room.refectory)

# summer4
s.new_day()
s.inventory_add(
    liquid.paint_moth_gold,
)
s.upgrade(skill.transformations_and_liberations, using=lesson.inks_of_revelation)
s.master(codex.nyns_cages_bruges_text)
s.upgrade(skill.drums_and_dances, using=lesson.quenchings_and_quellings)
s.inventory_remove(
    beverage.schloss_jannings_glass,
    beverage.ch_second_flush_assam_cup,
)
s.upgrade(skill.drums_and_dances, using=lesson.quenchings_and_quellings)
s.master(codex.cucurbit_prisoner_records_1928)
s.upgrade(skill.edicts_martial, using=lesson.hill_and_hollow)
s.unlock(room.lesser_bridge)
s.master(codex.the_alloy_of_the_white_rose)

# summer5
s.new_day()
s.upgrade(skill.edicts_martial, using=lesson.hill_and_hollow)
s.inventory_remove(
    beverage.ch_second_flush_assam_cup,
    beverage.trn_limited_drinking_cocoa_cup,
)
s.upgrade(skill.ouranoscopy, using=lesson.purifications_and_exaltations)
s.master(codex.inaam_kapigiginlupir_garkie_cryppys)
s.unlock(room.gaol_yard)
s.upgrade(skill.ouranoscopy, using=lesson.purifications_and_exaltations)
s.master(codex.the_gospel_of_zacchaeus)
s.upgrade(skill.solutions_and_separations, using=lesson.transformations_and_liberations)
s.upgrade(skill.ouranoscopy, using=lesson.applebright_euphonies)
s.unlock(room.stores)

# summer6
s.new_day()
s.master(codex.a_journey_to_the_grove)
s.inventory_remove(
    beverage.isle_water_glass,
    beverage.isle_water_glass,
    candle.widows_candle,
)
s.upgrade(skill.solutions_and_separations, using=lesson.horns_and_ivories)
s.upgrade(skill.leaves_and_thorns, using=lesson.orchids_and_narcotics)
s.master(codex.enchiridion_tragularis)
s.unlock(room.tower_clock)
s.upgrade(skill.ouranoscopy, using=lesson.serpents_and_venoms)
s.upgrade(skill.ouranoscopy, using=lesson.serpents_and_venoms)
s.unlock(room.back_stairs)

# autumn1
s.new_day(season=season.autumn)
s.inventory_remove(
    beverage.solomons_preparation,
    candle.historywax_candle,
    candle.small_candlestick,
    beverage.ch_second_flush_assam_cup,
)
s.upgrade(skill.solutions_and_separations, using=lesson.horns_and_ivories)
s.unlock(room.gaol_hall)
s.upgrade(skill.transformations_and_liberations, using=lesson.transformations_and_liberations)
s.master(codex.the_scar_in_the_sky)
s.upgrade(skill.drums_and_dances, using=lesson.quenchings_and_quellings)
s.inventory_add(
    skill.deep_mandaic,
    liquid.amethyst_ampoule,
)
s.commit(skill.deep_mandaic, wisdom="ithastry")

# autumn2
s.new_day()
s.inventory_remove(
    flower.blue_crown,
    beverage.isle_water_glass,
)
s.upgrade(skill.drums_and_dances, using=lesson.quenchings_and_quellings)
s.catalogue(
    reel_of_film.the_open_head,
    phonograph_record.opening_the_sky,
    codex.the_locksmiths_dream_trespasses,
    codex.the_locksmiths_dream_portions_and_proportions,
    codex.the_rose_of_waznei,
)
s.unlock(room.gaol_kitchen)
s.master(phonograph_record.recordings_from_the_althiban_abyss)
s.master(codex.the_locksmiths_dream_trespasses)
s.master(codex.commandments_for_the_preservation_of_all_that_exists)
s.master(codex.the_locksmiths_dream_portions_and_proportions)
s.inventory_add(
    device.flushed_mommet,
)
s.unlock(room.servants_quarters_north)

# autumn3
s.new_day()
s.inventory_remove(
    candle.tall_candlestick,
    candle.tall_candlestick,
    beverage.ch_second_flush_assam_cup,
    material.driftwood_fragment,
    liquid.stargall_ink,
    flower.vase_of_lilies,
)
s.upgrade(skill.drums_and_dances, using=lesson.stitching_and_binding)
s.upgrade(skill.ouranoscopy, using=lesson.lockworks_and_clockworks)
s.inventory_add(
    codex.the_orchid_transfigurations_a_birth,
    tool.mazarine_fife,
)
s.master(codex.nyns_cages_avignon_text)
s.master(codex.the_rose_of_waznei)
s.master(codex.the_iron_book)
s.upgrade(skill.drums_and_dances, using=lesson.quenchings_and_quellings)
s.upgrade(skill.preliminal_meter, using=lesson.edicts_liminal)
s.upgrade(skill.inks_of_revelation, using=lesson.auroral_contemplations)
s.unlock(room.gaol_cellar)

# autumn4
s.new_day()
s.inventory_remove(
    material.yew_blank,
    beverage.ch_second_flush_assam_cup,
)
s.inventory_add(
    tool.mazarine_fife,
    material.granite_slab,
)
s.upgrade(skill.stitching_and_binding, using=lesson.quenchings_and_quellings)
s.master(codex.the_orchid_transfigurations_a_birth)
s.upgrade(skill.auroral_contemplations, using=lesson.disciplines_of_the_hammer)
s.upgrade(skill.stitching_and_binding, using=lesson.quenchings_and_quellings)
s.master(codex.a_second_glory)
s.upgrade(skill.serpents_and_venoms, using=lesson.snow_stories)
s.upgrade(skill.serpents_and_venoms, using=lesson.snow_stories)
s.upgrade(skill.leaves_and_thorns, using=lesson.resurgences_and_emergences)
s.unlock(room.gullscry_loggia)

# autumn5
s.new_day()
s.inventory_remove(
    beverage.ch_second_flush_assam_cup,
)
s.master(codex.from_history_to_eternity)
s.inventory_add(
    material.bitterblack_salts,
    tool.mazarine_fife,
)
s.upgrade(skill.auroral_contemplations, using=lesson.inks_of_revelation)
s.master(codex.the_red_book_of_brittany)
s.master(codex.the_white_book_of_brittany)
s.unlock(room.gullscry_tower_valentines_room)
s.upgrade(skill.leaves_and_thorns, using=lesson.resurgences_and_emergences)
s.upgrade(skill.serpents_and_venoms, using=lesson.inks_of_power)

# autumn6
s.new_day()
s.inventory_add(
    beverage.skinshuck_mead,
    sustenance.dark_marrow,
)
s.upgrade(skill.serpents_and_venoms, using=lesson.inks_of_power)
s.inventory_remove(
    beverage.veiled_goddess_lapsang_souchong_cup,
    beverage.solomons_preparation,
)
s.master(codex.the_debate_of_seven_cups)
s.upgrade(skill.ragged_crossroads, using=lesson.ragged_crossroads)
s.master(codex.the_world_does_not_weep)
s.unlock(room.gullscry_tower_eales_room)
s.upgrade(skill.preliminal_meter, using=lesson.solutions_and_separations)
s.upgrade(skill.serpents_and_venoms, using=lesson.putrefactions_and_calcinations)

# winter1
s.new_day(season=season.winter)
s.inventory_remove(
    beverage.veiled_goddess_lapsang_souchong_cup,
)
s.inventory_add(
    thing.yellowing_newspaper,
    beverage.domaine_raveline_bottle,
    skill.ramsund,
    liquid.nillycant,
)
s.master(phonograph_record.opening_the_sky)
s.upgrade(skill.serpents_and_venoms, using=lesson.putrefactions_and_calcinations)
s.catalogue(
    codex.the_other_line,
    codex.the_carmine_petal_unexpurgated,
)
s.unlock(room.bells)
s.upgrade(skill.ragged_crossroads, using=lesson.ragged_crossroads)
s.upgrade(skill.stitching_and_binding, using=lesson.strings_and_songs)
s.commit(skill.ramsund, wisdom="birdsong")

# winter2
s.new_day()
s.inventory_remove(
    beverage.skinshuck_mead,
    liquid.cuckoo_honey,
    beverage.armagnac_dys_glass,
)
s.upgrade(skill.stitching_and_binding, using=lesson.strings_and_songs)
s.master(codex.the_other_line)
s.upgrade(skill.preliminal_meter, using=lesson.solutions_and_separations)
s.master(codex.book_of_true_blood)
s.master(codex.on_the_winding_stair)
s.inventory_add(
    beverage.roscraggan_whisky_bottle,
    material.dawnlion_coffee_packet,
)
s.upgrade(skill.ragged_crossroads, using=lesson.meniscate_reflections)
s.upgrade(skill.preliminal_meter, using=lesson.door_and_wall)
s.unlock(room.spire)
s.unlock(room.hidden_stair)

# winter3
s.new_day()
s.inventory_remove(
    beverage.dawnlion_coffee_cup,
    beverage.armagnac_dys_glass,
)
s.inventory_add(
    mark.year_tally,
)
s.upgrade(skill.ragged_crossroads, using=lesson.meniscate_reflections)
s.master(codex.the_carmine_petal_revised)
s.unlock(room.whispering_stair)
s.upgrade(skill.preliminal_meter, using=lesson.door_and_wall)
s.unlock(room.our_lady_beneath)
s.upgrade(skill.auroral_contemplations, using=lesson.inks_of_revelation)
s.unlock(room.gullscry_tower_summit)

# winter4
s.new_day()
s.upgrade(skill.ragged_crossroads, using=lesson.disciplines_of_the_hammer)
s.inventory_add(
    material.wire_silver,
)
s.master(codex.the_book_of_masks)
s.unlock(room.staff_room)
s.upgrade(skill.preliminal_meter, using=lesson.preliminal_meter)

# winter5
s.new_day()
s.inventory_add(
    remains.animal_bones,
    sustenance.pale_marrow,
    material.trn_limited_drinking_cocoa_packet,
    beverage.rubywise_ruin,
    flower.lenten_rose,
)
s.upgrade(skill.stitching_and_binding, using=lesson.weaving_and_knotworking)
s.malady(soul.health)
s.inventory_remove(
    beverage.dawnlion_coffee_cup,
)
s.unlock(room.crucible_tower_governors_office)
s.upgrade(skill.auroral_contemplations, using=lesson.disciplines_of_the_hammer)
s.upgrade(skill.inks_of_revelation, using=lesson.weaving_and_knotworking)
s.catalogue(
    codex.the_tantra_of_worms,
    codex.cucurbit_prisoner_records_1927,
    codex.singlefoot_songs,
)
s.upgrade_soul(soul.trist, to_level=2, using=skill.ramsund)

# winter6
s.new_day()
s.inventory_remove(
    material.gervinite,
    beverage.witching_tisane,
)
s.inventory_add(
    flower.lenten_rose,
    material.serpentinite_slab,
    soul.wist,
)
s.master(codex.the_tantra_of_worms)
s.upgrade(skill.stone_stories, using=lesson.coil_and_chasm)
s.master(codex.singlefoot_songs)
s.master(codex.cucurbit_prisoner_records_1927)
s.upgrade(skill.stone_stories, using=lesson.insects_and_nectars)
s.unlock(room.earth_cellar)
s.upgrade(skill.stone_stories, using=lesson.coil_and_chasm)
s.unlock(room.crucible_tower_governors_quarters)
s.catalogue(
    codex.de_bellis_murorum,
    codex.on_the_white,
    reel_of_film.experiment_beyond_sight,
    codex.travelling_at_night_vol_3,
    codex.the_locksmiths_dream_incursus,
)

# spring1
s.new_day(season=season.spring)
s.inventory_remove(
    beverage.veiled_goddess_lapsang_souchong_cup,
)
s.master(codex.de_bellis_murorum)
s.upgrade(skill.stone_stories, using=lesson.hill_and_hollow)
s.master(codex.travelling_at_night_vol_3)
s.master(codex.the_locksmiths_dream_incursus)
s.upgrade(skill.preliminal_meter, using=lesson.door_and_wall)
s.upgrade_soul(soul.wist, to_level=2, using=skill.snow_stories)
s.unlock(room.earl_brians_field)
s.master(codex.on_the_white)
s.master(codex.the_chandlers_wish)
s.master(reel_of_film.experiment_beyond_sight)
s.upgrade(skill.disciplines_of_the_scar, using=lesson.inks_of_revelation)
s.upgrade(skill.disciplines_of_the_scar, using=lesson.inks_of_revelation)
s.inventory_add(
    skill.sabazine,
)
s.commit(skill.disciplines_of_the_scar, wisdom="illumination")

# spring2
s.new_day()
s.inventory_remove(
    sustenance.hens_egg,
    beverage.mist_kissed_water_glass,
    material.gervinite,
    leaf.vase_of_gorse,
    beverage.veiled_goddess_lapsang_souchong_cup,
)
s.upgrade(skill.insects_and_nectars, using=lesson.edicts_inviolable)
s.upgrade(skill.stone_stories, using=lesson.insects_and_nectars)
s.inventory_add(
    beast.chimeric_larva,
    flower.catsclaw,
    flower.moth_orchid,
    material.serpentinite_slab,
)
s.upgrade(skill.insects_and_nectars, using=lesson.edicts_inviolable)
s.unlock(room.cell_adepts)
s.master(codex.towards_a_fundamental_aesthetic)
s.catalogue(
    codex.the_book_of_thrones,
    reel_of_film.the_admonitory_automata_project,
    codex.glimmerings,
)
s.upgrade(skill.ragged_crossroads, using=lesson.quenchings_and_quellings)
s.master(codex.an_echo_of_silence)
s.unlock(room.gull_colony)

# spring3
s.new_day()
s.upgrade(skill.glaziery_and_lightsmithing, using=lesson.glassblowing_and_vesselcrafting)
s.upgrade(skill.glaziery_and_lightsmithing, using=lesson.glassblowing_and_vesselcrafting)
s.inventory_add(
    flower.catsclaw,
)
s.inventory_remove(
    liquid.turpentine,
    material.gervinite,
    material.wire_copper,
)
s.upgrade(skill.glaziery_and_lightsmithing, using=lesson.sacra_limiae)
s.master(codex.glimmerings)
s.master(codex.unhatched_hymns)
s.commit(skill.glaziery_and_lightsmithing, wisdom="illumination")
s.upgrade(skill.auroral_contemplations, using=lesson.sacra_solis_invicti)
s.unlock(room.upper_pump_room)
s.unlock(room.hermit_cell)
s.upgrade(skill.auroral_contemplations, using=lesson.sacra_solis_invicti)
s.catalogue(
    codex.the_deaths_of_the_moon,
    codex.in_memory_of_gods,
    codex.the_book_of_dissolution,
)
s.master(reel_of_film.the_admonitory_automata_project)

# spring4
s.new_day()
s.inventory_remove(
    leaf.vase_of_gorse,
    flower.vase_of_lilies,
    candle.moth_orchid_scented_candle,
    beverage.dandelion_wine_glass,
    beast.chimeric_larva,
)
s.upgrade(skill.lockworks_and_clockworks, using=lesson.lockworks_and_clockworks)
s.upgrade(skill.ragged_crossroads, using=lesson.sights_and_sensations)
s.unlock(room.rowenarium)
s.master(codex.deaths_and_their_evasions)
s.upgrade(skill.lockworks_and_clockworks, using=lesson.lockworks_and_clockworks)
s.inventory_add(
    codex.towards_a_fundamental_aesthetic_second_edition,
    sustenance.viper_egg,
    remains.mackerel,
    codex.the_three_and_the_three_st_chiavi_manuscript,
    liquid.honey,
    beast.perilous_imago,
)
s.unlock(room.lower_pump_room)
s.unlock(room.silver_vault)

###############################################################################################
json.dump(minimize_app_state(app_state_from_boh(s, inventory_addition, inventory_removal)), open("sample_late.json", "w"), indent=2)

# spring5
s.new_day()
s.upgrade(skill.lockworks_and_clockworks, using=lesson.edicts_liminal)
s.master(codex.towards_a_fundamental_aesthetic_second_edition)
s.master(codex.the_turquoise_hand)
s.upgrade(skill.lockworks_and_clockworks, using=lesson.sights_and_sensations)
s.master(scroll.shuritic_book_of_suns)
s.inventory_add(
    liquid.marakat,
    fruit.pyrus_auricalcinus,
)
s.unlock(room.crucible_tower_interview_laboratory)
s.upgrade(skill.lockworks_and_clockworks, using=lesson.sights_and_sensations)
s.catalogue(
    codex.sunset_passages,
)

# spring6
s.new_day()
s.upgrade(skill.lockworks_and_clockworks, using=lesson.sacra_solis_invicti)
s.inventory_remove(
    candle.tall_candlestick,
    beverage.skinshuck_mead,
)
s.unlock(room.cell_long)
s.master(codex.the_three_and_the_three_st_chiavi_manuscript)
s.upgrade(skill.auroral_contemplations, using=lesson.sacra_solis_invicti)
s.catalogue(
    codex.on_the_matter_and_the_deeds_of_serpents,
    codex.the_skeleton_songs,
)
s.unlock(room.cell_question)

# summer1
s.new_day(season=season.summer)
s.upgrade(skill.stone_stories, using=lesson.pentiments_and_precursors)
s.upgrade(skill.insects_and_nectars, using=lesson.edicts_inviolable)
s.master(codex.the_skeleton_songs)
s.unlock(room.columbic_crypt)
s.master(codex.sunset_passages)
s.inventory_add(
    material.ambergris_chunk,
)
s.upgrade(skill.insects_and_nectars, using=lesson.edicts_inviolable)
s.unlock(room.hall_of_voices)

# summer2
s.new_day()
s.unlock(room.oubliette)
s.upgrade(skill.auroral_contemplations, using=lesson.sacra_solis_invicti)
s.inventory_remove(
    flower.vase_of_amaryllis,
    material.ambergris_chunk,
)
s.inventory_add(
    tablet.the_suns_design,
    flower.lenten_rose,
)
s.upgrade(skill.edicts_liminal, using=lesson.edicts_liminal)
s.unlock(room.catacombs)
s.catalogue(
    codex.the_sevenfold_slaying_of_the_seven_coiled,
)
s.master(tablet.the_suns_design)

# summer3
s.new_day()
s.upgrade(skill.insects_and_nectars, using=lesson.edicts_inviolable)
s.inventory_remove(
    beverage.armagnac_dys_glass,
    beverage.mist_kissed_water_glass,
    sustenance.pickled_pilchards,
)
s.inventory_add(
    material.wire_orichalcum,
)
s.upgrade(skill.stone_stories, using=lesson.pentiments_and_precursors)
s.unlock(room.ivory_vault)
s.upgrade(skill.edicts_liminal, using=lesson.resurgences_and_emergences)
s.upgrade(skill.sights_and_sensations, using=lesson.watchmans_paradoxes)
s.master(codex.the_sky_in_the_scar)
s.unlock(room.boathouse)
s.catalogue(
    codex.the_hissing_key,
)

# summer4
s.new_day()
s.inventory_remove(
    liquid.paraffin,
    beverage.sacrament_ascite,
)
s.inventory_add(
    liquid.uzult,
    beast.living_relic,
)
s.upgrade(skill.sights_and_sensations, using=lesson.sights_and_sensations)
s.upgrade(skill.sights_and_sensations, using=lesson.watchmans_paradoxes)
s.unlock(room.iron_vault)
s.master(codex.the_hissing_key)
s.upgrade(skill.insects_and_nectars, using=lesson.sickle_and_eclipse)
s.unlock(room.cell_worm_inhabited)

# summer5
s.new_day()
s.unlock(room.sea_caves)
s.inventory_remove(
    liquid.honey,
    material.lignum_vitae_blank,
)
s.inventory_add(
    scroll.the_sun_disfigured,
    tablet.serpent_root,
)
s.upgrade(skill.insects_and_nectars, using=lesson.sickle_and_eclipse)
s.master(tablet.serpent_root)
s.upgrade(skill.insects_and_nectars, using=lesson.rites_of_the_roots)
s.upgrade(skill.inks_of_power, using=lesson.serpents_and_venoms)
s.unlock(room.deeplight_caves)
s.unlock(room.smugglers_den)

# summer6
s.new_day()
s.upgrade(skill.inks_of_power, using=lesson.serpents_and_venoms)
s.master(scroll.the_sun_disfigured)
s.inventory_remove(
    device.pale_mommet,
    beverage.rubywise_ruin,
    beverage.leathy,
    liquid.cuckoo_honey,
)
s.upgrade(skill.sights_and_sensations, using=lesson.applebright_euphonies)
s.master(tablet.amiranis_beteli)
s.unlock(room.chapel_calicite)
s.catalogue(
    codex.skin_of_silver,
    codex.the_songs_of_the_carapace_cross,
    codex.book_of_miah,
    codex.how_the_end_will_begin,
    codex.the_larquebine_codex,
)
s.upgrade(skill.meniscate_reflections, using=lesson.bells_and_brazieries)
s.upgrade(skill.sights_and_sensations, using=lesson.applebright_euphonies)
s.upgrade(skill.meniscate_reflections, using=lesson.bells_and_brazieries)
s.unlock(room.shrine_to_st_tentreto)

# numa1
s.new_day(season=season.numa)
s.master(codex.the_larquebine_codex)
s.skill_reset(skill.inks_of_containment)
s.upgrade(skill.sea_stories, using=lesson.a_lesson_of_many_facets)
s.inventory_remove(
    candle.widows_candle,
    candle.widows_candle,
    candle.widows_candle,
)
s.commit(skill.sea_stories, wisdom="birdsong")
s.upgrade(skill.pentiments_and_precursors, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.inks_of_containment, using=lesson.a_lesson_of_many_facets)
s.malady(soul.trist)
s.upgrade(skill.inks_of_containment, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.pentiments_and_precursors, using=lesson.a_lesson_of_many_facets)
s.malady(soul.chor)
s.upgrade(skill.inks_of_containment, using=lesson.a_lesson_of_many_facets)
s.commit(skill.pentiments_and_precursors, wisdom="birdsong")
s.inventory_add(
    fruit.pyrus_auricalcinus,
    skill.hyksos,
    beverage.mist_kissed_water_pitcher,
)
s.upgrade(skill.sabazine, using=lesson.a_lesson_of_many_facets)
s.malady(soul.wist)
s.commit(skill.sabazine, wisdom="horomachistry")
s.upgrade(skill.inks_of_containment, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.inks_of_revelation, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.inks_of_revelation, using=lesson.a_lesson_of_many_facets)
s.malady(soul.phost)
s.inventory_remove(
    lesson.a_lesson_of_many_facets,
    lesson.a_lesson_of_many_facets,
    lesson.a_lesson_of_many_facets,
)

# autumn1
s.new_day(season=season.autumn)
s.skill_reset(skill.inks_of_containment)
s.upgrade(skill.inks_of_containment, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.bells_and_brazieries, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.inks_of_containment, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.bells_and_brazieries, using=lesson.a_lesson_of_many_facets)
s.commit(skill.bells_and_brazieries, wisdom="horomachistry")
s.upgrade(skill.inks_of_containment, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.sacra_limiae, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.inks_of_containment, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.meniscate_reflections, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.sacra_limiae, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.sacra_limiae, using=lesson.a_lesson_of_many_facets)
s.inventory_add(
    flower.honeyscar_jasmine,
    thing.the_writing_on_the_wall,
)
s.commit(skill.sacra_limiae, wisdom="horomachistry")
s.commit(skill.the_great_signs_and_the_great_scars, wisdom="horomachistry")
s.upgrade(skill.meniscate_reflections, using=lesson.a_lesson_of_many_facets)
s.commit(skill.meniscate_reflections, wisdom="illumination")
s.upgrade(skill.inks_of_power, using=lesson.a_lesson_of_many_facets)
s.inventory_remove(
    lesson.a_lesson_of_many_facets,
)

# autumn2
s.new_day()
s.master(codex.a_childs_treasury_of_golden_afternoons)
s.upgrade(skill.pearl_and_tide, using=lesson.sharps)
s.inventory_remove(
    liquid.catwink,
    sustenance.pickled_pilchards,
    sustenance.pickled_pilchards,
    candle.widows_candle,
    beverage.armagnac_dys_glass,
    remains.mackerel,
)
s.upgrade(skill.pearl_and_tide, using=lesson.sharps)
s.master(codex.skin_of_silver)
s.upgrade(skill.spices_and_savours, using=lesson.disciplines_of_the_hammer)
s.unlock(room.chapel_ascite)
s.upgrade(skill.spices_and_savours, using=lesson.disciplines_of_the_hammer)
s.master(reel_of_film.the_open_head)
s.master(codex.the_dream_of_the_conspiracy_of_the_lower_skies)
s.catalogue(
    codex.the_sky_the_soul,
    codex.as_the_sun_his_course,
    codex.where_has_she_gone,
    codex.a_manual_for_departure,
)
s.upgrade(skill.sacra_solis_invicti, using=lesson.disciplines_of_the_scar)
s.upgrade(skill.sacra_solis_invicti, using=lesson.disciplines_of_the_scar)
s.master(codex.my_deeds_my_powers_my_achievements_and_the_injustices_perpetrated_against_me)
s.upgrade(skill.hyksos, using=lesson.the_great_signs_and_the_great_scars)
s.upgrade(skill.resurgences_and_emergences, using=lesson.the_great_signs_and_the_great_scars)
s.upgrade(skill.spices_and_savours, using=lesson.transformations_and_liberations)
s.unlock(room.loading_dock)

# autumn3
s.new_day()
s.master(codex.as_the_sun_his_course)
s.upgrade(skill.anbary_and_lapidary, using=lesson.transformations_and_liberations)
s.master(codex.the_sky_the_soul)
s.upgrade(skill.spices_and_savours, using=lesson.transformations_and_liberations)
s.inventory_remove(
    beverage.mist_kissed_water_glass,
)
s.commit(skill.spices_and_savours, wisdom="ithastry")
s.commit(skill.stitching_and_binding, wisdom="ithastry")
s.commit(skill.inks_of_revelation, wisdom="ithastry")
s.upgrade(skill.anbary_and_lapidary, using=lesson.pyroglyphics)
s.upgrade(skill.sacra_solis_invicti, using=lesson.pyroglyphics)
s.upgrade(skill.pearl_and_tide, using=lesson.sickle_and_eclipse)
s.inventory_add(codex.the_five_letters_on_memory)
s.inventory_add(
    beverage.witching_tisane,
)
s.unlock(room.narthex)
s.master(codex.isaac_of_karths_history_of_the_shadowless_kings)
s.upgrade(skill.pearl_and_tide, using=lesson.sickle_and_eclipse)
s.upgrade(skill.door_and_wall, using=lesson.the_great_signs_and_the_great_scars)
s.upgrade(skill.desires_and_dissolutions, using=lesson.sand_stories)
s.master(codex.the_ascendant)
s.master(codex.the_black_book_of_brittany)
s.upgrade(skill.inks_of_power, using=lesson.sand_stories)
s.unlock(room.chapel_malachite)
s.upgrade(skill.desires_and_dissolutions, using=lesson.edicts_martial)
s.master(codex.the_five_letters_on_memory)

# autumn4
s.new_day()
s.upgrade(skill.desires_and_dissolutions, using=lesson.inks_of_containment)
s.catalogue(
    codex.the_book_of_the_white_cat,
    codex.the_voyages_of_ferninshun_of_oreol,
)
s.upgrade(skill.disciplines_of_the_hammer, using=lesson.edicts_martial)
s.upgrade(skill.edicts_inviolable, using=lesson.inks_of_containment)
s.upgrade(skill.edicts_inviolable, using=lesson.rhyme_and_remembrance)
s.master(codex.a_descent_of_the_shell)
s.upgrade(skill.sacra_solis_invicti, using=lesson.purifications_and_exaltations)
s.master(codex.in_memory_of_gods)
s.upgrade(skill.disciplines_of_the_hammer, using=lesson.ragged_crossroads)
s.master(codex.book_of_miah)
s.upgrade(skill.sacra_solis_invicti, using=lesson.purifications_and_exaltations)
s.commit(skill.sacra_solis_invicti, wisdom="horomachistry")
s.commit(skill.ouranoscopy, wisdom="horomachistry")
s.upgrade(skill.inks_of_power, using=lesson.sand_stories)
s.master(codex.the_carmine_petal_unexpurgated)
s.master(codex.the_high_mysteries_of_the_innermost_chamber_of_our_church_solar)
s.upgrade(skill.putrefactions_and_calcinations, using=lesson.ragged_crossroads)
s.upgrade(skill.putrefactions_and_calcinations, using=lesson.sand_stories)
s.master(codex.journal_of_sir_david_greene)
s.master(codex.medusas_lament)

# autumn5
s.new_day()
s.upgrade(skill.anbary_and_lapidary, using=lesson.disciplines_of_the_hammer)
s.upgrade(skill.anbary_and_lapidary, using=lesson.disciplines_of_the_hammer)
s.upgrade_soul(soul.fet, to_level=2, using=skill.sabazine)
s.upgrade(skill.anbary_and_lapidary, using=lesson.sacra_solis_invicti)
s.upgrade(skill.coil_and_chasm, using=lesson.horns_and_ivories)
s.upgrade(skill.anbary_and_lapidary, using=lesson.disciplines_of_the_hammer)
s.master(codex.the_songs_of_the_carapace_cross)
s.upgrade(skill.horns_and_ivories, using=lesson.horns_and_ivories)
s.upgrade(skill.sharps, using=lesson.sharps)
s.upgrade(skill.anbary_and_lapidary, using=lesson.sacra_solis_invicti)
s.upgrade(skill.sand_stories, using=lesson.sharps)
s.upgrade(skill.rites_of_the_roots, using=lesson.edicts_liminal)
s.master(codex.the_sevenfold_slaying_of_the_seven_coiled)

# autumn6
s.new_day()
s.upgrade(skill.sickle_and_eclipse, using=lesson.disciplines_of_the_scar)
s.master(codex.the_book_of_dissolution)
s.commit(skill.anbary_and_lapidary, wisdom="ithastry")
s.commit(skill.transformations_and_liberations, wisdom="ithastry")
s.upgrade(skill.sharps, using=lesson.disciplines_of_the_scar)
s.upgrade(skill.rites_of_the_roots, using=lesson.transformations_and_liberations)
s.upgrade(skill.sickle_and_eclipse, using=lesson.disciplines_of_the_scar)
s.master(codex.the_voyages_of_ferninshun_of_oreol)
s.upgrade(skill.rites_of_the_roots, using=lesson.transformations_and_liberations)
s.upgrade(skill.applebright_euphonies, using=lesson.sea_stories)
s.upgrade(skill.rites_of_the_roots, using=lesson.edicts_liminal)
s.upgrade_soul(soul.phost, to_level=2, using=skill.disciplines_of_the_scar)
s.upgrade(skill.rhyme_and_remembrance, using=lesson.sea_stories)
s.master(codex.the_book_of_thrones)
s.upgrade(skill.watchmans_paradoxes, using=lesson.auroral_contemplations)
s.upgrade(skill.orchids_and_narcotics, using=lesson.sea_stories)
s.master(codex.twenty_six_enticements_seven_torments)

# winter1
s.new_day(season=season.winter)
s.master(codex.the_book_of_the_white_cat)
s.upgrade(skill.rites_of_the_roots, using=lesson.edicts_liminal)
s.master(codex.the_burning_woman)
s.upgrade(skill.glassblowing_and_vesselcrafting, using=lesson.watchmans_paradoxes)
s.upgrade(skill.door_and_wall, using=lesson.transformations_and_liberations)
s.upgrade(skill.rites_of_the_roots, using=lesson.resurgences_and_emergences)
s.upgrade(skill.sky_stories, using=lesson.watchmans_paradoxes)
s.upgrade(skill.glassblowing_and_vesselcrafting, using=lesson.watchmans_paradoxes)
s.upgrade(skill.watchmans_paradoxes, using=lesson.auroral_contemplations)

# winter2
s.new_day()
s.upgrade(skill.rites_of_the_roots, using=lesson.resurgences_and_emergences)
s.upgrade(skill.rites_of_the_roots, using=lesson.transformations_and_liberations)

# winter3
s.new_day()
s.inventory_add(phonograph_record.the_invisible_opera_unfinished_recording)
s.master(phonograph_record.the_invisible_opera_unfinished_recording)

# winter4
s.new_day()
s.upgrade(skill.applebright_euphonies, using=lesson.strings_and_songs)
s.upgrade(skill.applebright_euphonies, using=lesson.strings_and_songs)

# winter5, 6, spring1, 2, 3, 4, 5, 6
s.inventory_add(codex.the_tripled_heart)

# numa2
s.new_day(season=season.numa)
s.skill_reset(skill.inks_of_containment)
s.upgrade(skill.inks_of_containment, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.inks_of_containment, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.inks_of_containment, using=lesson.a_lesson_of_many_facets)
s.malady(soul.phost)
s.upgrade(skill.inks_of_containment, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.horns_and_ivories, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.inks_of_power, using=lesson.a_lesson_of_many_facets)
s.inventory_add(
    skill.kernewek_henavek,
)
s.upgrade(skill.coil_and_chasm, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.inks_of_power, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.herbs_and_infusions, using=lesson.a_lesson_of_many_facets)
s.inventory_remove(
    candle.widows_candle,
    lesson.a_lesson_of_many_facets,
    lesson.a_lesson_of_many_facets,
    lesson.a_lesson_of_many_facets,
    lesson.a_lesson_of_many_facets,
)
s.master(codex.the_tripled_heart)

# autumn1
s.new_day(season=season.autumn)
s.skill_reset(skill.inks_of_containment)
s.upgrade(skill.inks_of_containment, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.inks_of_containment, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.tridesma_hiera, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.inks_of_containment, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.tridesma_hiera, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.inks_of_containment, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.inks_of_power, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.tridesma_hiera, using=lesson.a_lesson_of_many_facets)
s.inventory_add(
    skill.killasimi,
)
s.upgrade(skill.herbs_and_infusions, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.tridesma_hiera, using=lesson.a_lesson_of_many_facets)
s.commit(skill.tridesma_hiera, wisdom="preservation")
s.commit(skill.desires_and_dissolutions, wisdom="the_bosk")
s.upgrade(skill.herbs_and_infusions, using=lesson.a_lesson_of_many_facets)
s.commit(skill.herbs_and_infusions, wisdom="preservation")
s.upgrade(skill.coil_and_chasm, using=lesson.a_lesson_of_many_facets)
s.inventory_remove(
    lesson.a_lesson_of_many_facets,
)

# autumn2
s.new_day()
s.master(codex.the_deaths_of_the_moon)
s.upgrade(skill.killasimi, using=lesson.snow_stories)
s.master(codex.ud_rocashaas)
s.upgrade(skill.rhyme_and_remembrance, using=lesson.snow_stories)
s.upgrade(skill.coil_and_chasm, using=lesson.stone_stories)
s.upgrade(skill.coil_and_chasm, using=lesson.stone_stories)
s.master(codex.two_wombs_one_heart)
s.upgrade(skill.edicts_inviolable, using=lesson.stitching_and_binding)
s.upgrade(skill.edicts_inviolable, using=lesson.stitching_and_binding)

# autumn3
s.new_day()
s.master(tablet.kopralith_omphalos)
s.upgrade(skill.edicts_inviolable, using=lesson.weaving_and_knotworking)
s.upgrade(skill.edicts_inviolable, using=lesson.weaving_and_knotworking)
s.inventory_add(codex.the_shaven_lock_tantra)
s.master(codex.the_shaven_lock_tantra)
s.upgrade(skill.coil_and_chasm, using=lesson.rites_of_the_roots)

# autumn4, 5, 6, winter1
s.new_day(season=season.winter)
s.inventory_add(
    skill.vak,
)
s.master(thing.the_writing_on_the_wall)
s.upgrade(skill.coil_and_chasm, using=lesson.spices_and_savours)
s.upgrade(skill.coil_and_chasm, using=lesson.spices_and_savours)
s.master(codex.on_the_matter_and_the_deeds_of_serpents)
s.upgrade(skill.horns_and_ivories, using=lesson.edicts_liminal)
s.upgrade(skill.edicts_liminal, using=lesson.edicts_liminal)
s.commit(skill.killasimi, wisdom="skolekosophy")
s.commit(skill.rhyme_and_remembrance, wisdom="skolekosophy")
s.commit(skill.horns_and_ivories, wisdom="skolekosophy")
s.commit(skill.edicts_inviolable, wisdom="preservation")
s.commit(skill.stone_stories, wisdom="preservation")
s.commit(skill.rites_of_the_roots, wisdom="preservation")
s.master(phonograph_record.a_tower_falls)
s.upgrade(skill.edicts_liminal, using=lesson.preliminal_meter)
s.commit(skill.edicts_liminal, wisdom="skolekosophy")

# winter3
s.new_day()
s.upgrade(skill.sand_stories, using=lesson.preliminal_meter)
s.upgrade_soul(soul.ereb, to_level=2, using=skill.killasimi)
s.upgrade_soul(soul.mettle, to_level=2, using=skill.sacra_limiae)
s.upgrade_soul(soul.health, to_level=2, using=skill.herbs_and_infusions)
s.upgrade(skill.sand_stories, using=lesson.preliminal_meter)
s.master(codex.a_manual_for_departure)
s.upgrade(skill.disciplines_of_the_hammer, using=lesson.door_and_wall)
s.upgrade(skill.kernewek_henavek, using=lesson.door_and_wall)
s.master(codex.the_origins_of_hours)
s.upgrade(skill.applebright_euphonies, using=lesson.sacra_limiae)
s.inventory_add(codex.the_orchid_transfigurations_noon)
s.commit(skill.applebright_euphonies, wisdom="the_bosk")
s.upgrade_soul(soul.chor, to_level=2, using=skill.pentiments_and_precursors)
s.upgrade(skill.watchmans_paradoxes, using=lesson.sacra_limiae)
s.upgrade(skill.watchmans_paradoxes, using=lesson.sacra_limiae)
s.master(codex.five_creations)
s.upgrade(skill.resurgences_and_emergences, using=lesson.resurgences_and_emergences)
s.master(codex.the_orchid_transfigurations_noon)

# winter4, 5
s.new_day()
s.upgrade(skill.resurgences_and_emergences, using=lesson.resurgences_and_emergences)
s.master(codex.how_the_end_will_begin)
s.upgrade(skill.disciplines_of_the_hammer, using=lesson.ragged_crossroads)
s.upgrade(skill.disciplines_of_the_hammer, using=lesson.ragged_crossroads)
s.master(codex.the_manner_in_which_the_alchemist_was_spared)
s.upgrade(skill.watchmans_paradoxes, using=lesson.anbary_and_lapidary)
s.upgrade(skill.watchmans_paradoxes, using=lesson.anbary_and_lapidary)
s.commit(skill.watchmans_paradoxes, wisdom="nyctodromy")
s.commit(skill.path_and_pilgrim, wisdom="nyctodromy")
s.commit(skill.coil_and_chasm, wisdom="nyctodromy")
s.master(codex.where_has_she_gone)
s.upgrade(skill.maggephene_mysteries, using=lesson.sand_stories)
s.upgrade(skill.maggephene_mysteries, using=lesson.sand_stories)
s.upgrade(skill.maggephene_mysteries, using=lesson.sand_stories)
s.commit(skill.maggephene_mysteries, wisdom="hushery")
s.master(phonograph_record.a_tower_rises)
s.upgrade(skill.glassblowing_and_vesselcrafting, using=lesson.preliminal_meter)
s.upgrade(skill.glassblowing_and_vesselcrafting, using=lesson.preliminal_meter)
s.upgrade(skill.glassblowing_and_vesselcrafting, using=lesson.preliminal_meter)

# spring3
s.new_day(season=season.spring)
s.inventory_add(codex.the_known_unknown_tantra)
s.master(codex.the_known_unknown_tantra)
s.upgrade(skill.sky_stories, using=lesson.watchmans_paradoxes)

# summer6
s.commit(skill.vak, wisdom="nyctodromy")
s.commit(skill.hyksos, wisdom="nyctodromy")
s.commit(skill.door_and_wall, wisdom="nyctodromy")
s.upgrade_soul(soul.shapt, to_level=2, using=skill.door_and_wall)

# autumn1,2,3
s.inventory_add(codex.the_suns_lament)
s.master(codex.the_suns_lament)
s.upgrade(skill.disciplines_of_the_hammer, using=lesson.ragged_crossroads)

# winter1-spring3
s.inventory_add(codex.calicite_supplications)
s.master(codex.calicite_supplications)
s.upgrade(skill.sharps, using=lesson.tridesma_hiera)
s.upgrade(skill.sharps, using=lesson.tridesma_hiera)
s.commit(skill.sharps, wisdom="hushery")
s.commit(skill.glassblowing_and_vesselcrafting, wisdom="hushery")
s.commit(skill.serpents_and_venoms, wisdom="hushery")
s.commit(skill.sights_and_sensations, wisdom="hushery")
s.commit(skill.inks_of_power, wisdom="hushery")
s.commit(skill.disciplines_of_the_hammer, wisdom="illumination")
s.commit(skill.preliminal_meter, wisdom="illumination")
s.commit(skill.auroral_contemplations, wisdom="illumination")
s.upgrade_soul(soul.phost, to_level=2, using=skill.auroral_contemplations)
s.upgrade_soul(soul.chor, to_level=2, using=skill.sea_stories)
s.upgrade_soul(soul.mettle, to_level=2, using=skill.bells_and_brazieries)
s.upgrade_soul(soul.ereb, to_level=2, using=skill.edicts_liminal)
s.upgrade_soul(soul.shapt, to_level=2, using=skill.coil_and_chasm)
s.upgrade_soul(soul.health, to_level=2, using=skill.quenchings_and_quellings)
s.upgrade_soul(soul.wist, to_level=2, using=skill.sights_and_sensations)
s.upgrade_soul(soul.trist, to_level=2, using=skill.ericapaean)
s.upgrade_soul(soul.fet, to_level=2, using=skill.ouranoscopy)

# autumn3
s.inventory_add(codex.journal_of_walter_dewulf)
s.master(codex.journal_of_walter_dewulf)
s.upgrade(skill.kernewek_henavek, using=lesson.door_and_wall)
s.commit(skill.kernewek_henavek, wisdom="ithastry")
s.upgrade_soul(soul.chor, to_level=3, using=skill.cracktrack)
s.upgrade_soul(soul.ereb, to_level=3, using=skill.rhyme_and_remembrance)
s.upgrade_soul(soul.fet, to_level=3, using=skill.the_great_signs_and_the_great_scars)
s.upgrade_soul(soul.health, to_level=3, using=skill.rites_of_the_roots)
s.upgrade_soul(soul.mettle, to_level=3, using=skill.disciplines_of_the_hammer)
s.upgrade_soul(soul.phost, to_level=3, using=skill.meniscate_reflections)
s.upgrade_soul(soul.shapt, to_level=3, using=skill.hyksos)
s.upgrade_soul(soul.trist, to_level=3, using=skill.inks_of_power)
s.upgrade_soul(soul.wist, to_level=3, using=skill.sharps)

# winter3
s.inventory_add(codex.the_queens_turn)
s.master(codex.the_queens_turn)
s.upgrade(skill.sickle_and_eclipse, using=lesson.hill_and_hollow)
s.commit(skill.sickle_and_eclipse, wisdom="nyctodromy")
s.upgrade(skill.sand_stories, using=lesson.hill_and_hollow)

# numa3 (summer1)
s.new_day(season=season.numa)
s.skill_reset(skill.inks_of_containment)
s.upgrade(skill.inks_of_containment, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.inks_of_containment, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.inks_of_containment, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.orchids_and_narcotics, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.inks_of_containment, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.orchids_and_narcotics, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.putrefactions_and_calcinations, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.orchids_and_narcotics, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.putrefactions_and_calcinations, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.orchids_and_narcotics, using=lesson.a_lesson_of_many_facets)
s.inventory_remove(
    lesson.a_lesson_of_many_facets,
    lesson.a_lesson_of_many_facets,
    lesson.a_lesson_of_many_facets,
)

# summer1
s.new_day(season=season.summer)
s.skill_reset(skill.inks_of_containment)
s.upgrade(skill.inks_of_containment, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.inks_of_containment, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.inks_of_containment, using=lesson.a_lesson_of_many_facets)
s.inventory_remove(
    candle.widows_candle,
)
s.upgrade(skill.inks_of_containment, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.resurgences_and_emergences, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.sky_stories, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.sand_stories, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.resurgences_and_emergences, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.putrefactions_and_calcinations, using=lesson.a_lesson_of_many_facets)
s.commit(skill.putrefactions_and_calcinations, wisdom="skolekosophy")
s.commit(skill.lockworks_and_clockworks, wisdom="skolekosophy")
s.commit(skill.solutions_and_separations, wisdom="skolekosophy")
s.commit(skill.ragged_crossroads, wisdom="skolekosophy")
s.commit(skill.resurgences_and_emergences, wisdom="the_bosk")
s.upgrade(skill.sky_stories, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.sky_stories, using=lesson.a_lesson_of_many_facets)
s.upgrade(skill.orchids_and_narcotics, using=lesson.a_lesson_of_many_facets)
s.commit(skill.orchids_and_narcotics, wisdom="the_bosk")
s.commit(skill.drums_and_dances, wisdom="the_bosk")
s.commit(skill.insects_and_nectars, wisdom="the_bosk")
s.inventory_remove(
    lesson.a_lesson_of_many_facets,
)

# summer3
s.inventory_add(codex.the_focus_of_amber)
s.master(codex.the_focus_of_amber)
s.upgrade(skill.sky_stories, using=lesson.glaziery_and_lightsmithing)

# autumn3
s.inventory_add(codex.the_crossing_to_noon)
s.master(codex.the_crossing_to_noon)
s.upgrade(skill.inks_of_containment, using=lesson.sea_stories)
s.upgrade(skill.inks_of_containment, using=lesson.sea_stories)

# winter3
s.inventory_add(codex.on_matthias_and_the_amethyst_imago_loss)
s.master(codex.on_matthias_and_the_amethyst_imago_loss)

# summer3
s.inventory_add(codex.the_carbonek_schism)
s.master(codex.the_carbonek_schism)

# autumn3
s.inventory_add(codex.the_serenity_of_the_black_wood)
s.master(codex.the_serenity_of_the_black_wood)

# winter3
s.inventory_add(codex.the_rose_of_nuriel)
s.master(codex.the_rose_of_nuriel)

# spring3
s.inventory_add(codex.ettery_after)
s.master(codex.ettery_after)
s.upgrade(skill.inks_of_containment, using=lesson.inks_of_containment)
s.commit(skill.inks_of_containment, wisdom="horomachistry")
s.commit(skill.edicts_martial, wisdom="horomachistry")

# summer3
s.inventory_add(codex.honey_the_comprehensive_guide)
s.master(codex.honey_the_comprehensive_guide)

# winter3
s.inventory_add(codex.the_secret_colours)
s.master(codex.the_secret_colours)

# spring3
s.inventory_add(codex.the_kerisham_portolan)
s.master(codex.the_kerisham_portolan)

# summer3
s.inventory_add(codex.the_three_and_the_three_vatican_manuscript)
s.master(codex.the_three_and_the_three_vatican_manuscript)

# numa5
s.inventory_remove(
    lesson.edicts_inviolable,
    lesson.edicts_inviolable,
    lesson.glaziery_and_lightsmithing,
    lesson.glaziery_and_lightsmithing,
    lesson.inks_of_containment,
    lesson.insects_and_nectars,
    lesson.sacra_limiae,
    lesson.sacra_limiae,
    lesson.sacra_limiae,
    lesson.sea_stories,
    lesson.sickle_and_eclipse,
    lesson.sickle_and_eclipse,
    lesson.solutions_and_separations,
    lesson.the_great_signs_and_the_great_scars,
    lesson.the_great_signs_and_the_great_scars,
)

# autumn3
s.inventory_add(codex.the_raptures_of_forculus)
s.master(codex.the_raptures_of_forculus)

# winter3
s.inventory_add(codex.the_berrybook)
s.master(codex.the_berrybook)

# summer3
s.inventory_add(codex.just_verse)
s.master(codex.just_verse)

# autumn3
s.inventory_add(codex.notes_on_bindings)
s.master(codex.notes_on_bindings)

# winter3
s.inventory_add(codex.the_history_of_inks)
s.master(codex.the_history_of_inks)

# spring3
s.inventory_add(codex.black_nephrite)
s.master(codex.black_nephrite)
s.upgrade(skill.wolf_stories, using=lesson.inks_of_power)
s.upgrade(skill.wolf_stories, using=lesson.inks_of_power)

# summer3
s.inventory_add(codex.an_introduction_to_histories)
s.master(codex.an_introduction_to_histories)
s.upgrade(skill.wolf_stories, using=lesson.snow_stories)

# winter3
s.inventory_add(codex.hunting_journals_of_bryan_dewulf)
s.master(codex.hunting_journals_of_bryan_dewulf)
s.upgrade(skill.wolf_stories, using=lesson.furs_and_feathers)
s.commit(skill.wolf_stories, wisdom="birdsong")
s.commit(skill.sand_stories, wisdom="birdsong")
s.commit(skill.strings_and_songs, wisdom="birdsong")
s.commit(skill.sky_stories, wisdom="birdsong")
s.commit(skill.pearl_and_tide, wisdom="nyctodromy")

# numa6
s.inventory_remove(
    lesson.furs_and_feathers,
    lesson.leaves_and_thorns,
    lesson.leaves_and_thorns,
    lesson.preliminal_meter,
    lesson.stitching_and_binding,
    lesson.stitching_and_binding,
    lesson.the_great_signs_and_the_great_scars,
)

# spring3
s.inventory_add(codex.the_world_despoild)
s.master(codex.the_world_despoild)

# summer3
s.inventory_add(codex.the_road_to_janus)
s.master(codex.the_road_to_janus)

# autumn3
s.inventory_add(codex.seven_shards)
s.master(codex.seven_shards)

# winter3
s.inventory_add(codex.the_treatise_on_underplaces)
s.master(codex.the_treatise_on_underplaces)

# summer3
s.inventory_add(codex.by_their_marks_shall_ye_know_them)
s.master(codex.by_their_marks_shall_ye_know_them)

# autumn3
s.inventory_add(scroll.the_watchful_tantra)
s.master(scroll.the_watchful_tantra)

# numa7
s.inventory_remove(
    lesson.disciplines_of_the_hammer,
    lesson.disciplines_of_the_hammer,
    lesson.door_and_wall,
    lesson.door_and_wall,
    lesson.door_and_wall,
    lesson.horns_and_ivories,
    lesson.maggephene_mysteries,
    lesson.purifications_and_exaltations,
    lesson.purifications_and_exaltations,
    lesson.surgeries_and_exsanguinations,
)

# winter3
s.inventory_add(codex.de_horis_book_1)
s.master(codex.de_horis_book_1)

# spring3
s.inventory_add(codex.a_novel_method_for_invocation_and_contrition)
s.master(codex.a_novel_method_for_invocation_and_contrition)

# summer3
s.inventory_add(codex.damascene_traditions_of_the_house_of_lethe)
s.master(codex.damascene_traditions_of_the_house_of_lethe)

# winter3
s.inventory_add(codex.ascite_supplications)
s.master(codex.ascite_supplications)

# spring3
s.inventory_add(codex.malachite_supplications)
s.master(codex.malachite_supplications)

# summer3
s.inventory_add(codex.de_horis_book_3)
s.master(codex.de_horis_book_3)

# numa8
s.inventory_remove(
    lesson.disciplines_of_the_scar,
    lesson.preliminal_meter,
    lesson.preliminal_meter,
    lesson.rites_of_the_roots,
    lesson.sacra_limiae,
    lesson.sacra_limiae,
    lesson.stone_stories,
    lesson.stone_stories,
    lesson.tridesma_hiera,
    lesson.tridesma_hiera,
)

# autumn3
s.inventory_add(codex.kitling_ripes_tasty_treats)
s.master(codex.kitling_ripes_tasty_treats)

# winter3
s.inventory_add(codex.on_thirstlies_ivories_and_lovelies)
s.master(codex.on_thirstlies_ivories_and_lovelies)

# summer3
s.inventory_add(codex.those_who_do_not_sleep)
s.master(codex.those_who_do_not_sleep)

# autumn3
s.inventory_add(codex.the_war_of_the_roads)
s.master(codex.the_war_of_the_roads)

# winter3
s.inventory_add(codex.a_pale_lady_and_a_prince_of_wines)
s.master(codex.a_pale_lady_and_a_prince_of_wines)

# spring3
s.inventory_add(codex.de_ratio_quercuum)
s.master(codex.de_ratio_quercuum)

# summer3
s.inventory_add(codex.the_grand_passage_of_the_hours)
s.master(codex.the_grand_passage_of_the_hours)

# winter3
s.inventory_add(codex.observations_on_the_peacock_door)
s.master(codex.observations_on_the_peacock_door)

# spring3
s.inventory_add(codex.the_instruments_of_the_heart)
s.master(codex.the_instruments_of_the_heart)

# summer3
s.inventory_add(codex.sunrise_awakenings)
s.master(codex.sunrise_awakenings)

# numa9
s.inventory_remove(
    lesson.auroral_contemplations,
    lesson.door_and_wall,
    lesson.door_and_wall,
    lesson.drums_and_dances,
    lesson.drums_and_dances,
    lesson.meniscate_reflections,
    lesson.resurgences_and_emergences,
    lesson.resurgences_and_emergences,
    lesson.rites_of_the_roots,
    lesson.rites_of_the_roots,
    lesson.sea_stories,
    lesson.sickle_and_eclipse,
    lesson.sickle_and_eclipse,
    lesson.spices_and_savours,
    lesson.surgeries_and_exsanguinations,
    lesson.surgeries_and_exsanguinations,
)

# autumn3
s.inventory_add(codex.the_silver_book)
s.master(codex.the_silver_book)

# winter3
s.inventory_add(scroll.the_flayed_tantra)
s.master(scroll.the_flayed_tantra)

# summer3
s.inventory_add(codex.the_book_of_the_extinguished_heart)
s.master(codex.the_book_of_the_extinguished_heart)

# autumn3
s.inventory_add(codex.the_messenger_awaiting_her_destination)
s.master(codex.the_messenger_awaiting_her_destination)

# winter3
s.inventory_add(codex.the_high_traditions_of_the_noble_endeavour)
s.master(codex.the_high_traditions_of_the_noble_endeavour)

# spring3
s.inventory_add(codex.the_account_of_kanishk_at_the_spiders_door)
s.master(codex.the_account_of_kanishk_at_the_spiders_door)

# summer3
s.inventory_add(codex.white_jade_tablet)
s.master(codex.white_jade_tablet)

# winter3
s.inventory_add(codex.the_three_and_the_three_kerisham_manuscript)
s.master(codex.the_three_and_the_three_kerisham_manuscript)

# spring3
s.inventory_add(codex.one_hundred_and_eight)
s.master(codex.one_hundred_and_eight)

# summer3
s.inventory_add(codex.the_geminiad_i)
s.master(codex.the_geminiad_i)

# autumn3
s.inventory_add(codex.the_geminiad_iii)
s.master(codex.the_geminiad_iii)

# winter3
s.inventory_add(codex.stolen_histories)
s.master(codex.stolen_histories)

# numa10
s.inventory_remove(
    lesson.coil_and_chasm,
    lesson.disciplines_of_the_hammer,
    lesson.door_and_wall,
    lesson.door_and_wall,
    lesson.door_and_wall,
    lesson.edicts_inviolable,
    lesson.edicts_inviolable,
    lesson.edicts_liminal,
    lesson.edicts_liminal,
    lesson.maggephene_mysteries,
    lesson.maggephene_mysteries,
    lesson.pentiments_and_precursors,
    lesson.quenchings_and_quellings,
    lesson.quenchings_and_quellings,
    lesson.quenchings_and_quellings,
    lesson.resurgences_and_emergences,
    lesson.resurgences_and_emergences,
    lesson.rites_of_the_roots,
    lesson.rites_of_the_roots,
    lesson.sharps,
    lesson.weaving_and_knotworking,
    lesson.weaving_and_knotworking,
)

# summer3
s.inventory_add(codex.rapt_in_the_king)
s.master(codex.rapt_in_the_king)

# autumn3
s.inventory_add(codex.one_thousand_threads)
s.master(codex.one_thousand_threads)

# winter3
s.inventory_add(codex.kitling_ripe_and_the_moldywarps_grave)
s.master(codex.kitling_ripe_and_the_moldywarps_grave)

# spring3
s.inventory_add(codex.the_other_eye_of_the_serpent)
s.master(codex.the_other_eye_of_the_serpent)

# summer3
s.inventory_add(codex.the_rose_of_hypatia)
s.master(codex.the_rose_of_hypatia)

# winter3
s.inventory_add(scroll.the_thirsting_tantra)
s.master(scroll.the_thirsting_tantra)

# numa11
s.inventory_remove(
    lesson.anbary_and_lapidary,
    lesson.anbary_and_lapidary,
    lesson.drums_and_dances,
    lesson.drums_and_dances,
    lesson.orchids_and_narcotics,
    lesson.orchids_and_narcotics,
    lesson.resurgences_and_emergences,
    lesson.tridesma_hiera,
    lesson.tridesma_hiera,
    lesson.weaving_and_knotworking,
    lesson.weaving_and_knotworking,
)

# spring3
s.inventory_add(codex.on_matthias_and_the_amethyst_imago_pursuit)
s.master(codex.on_matthias_and_the_amethyst_imago_pursuit)

# summer3
s.inventory_add(codex.oghkor_oghkor_tissilak_oghkor)
s.master(codex.oghkor_oghkor_tissilak_oghkor)

# autumn3
s.inventory_add(codex.on_matthias_and_the_amethyst_imago_transformation)
s.master(codex.on_matthias_and_the_amethyst_imago_transformation)

# winter3
s.inventory_add(codex.an_almanac_of_entrances)
s.master(codex.an_almanac_of_entrances)

# summer3
s.inventory_add(codex.de_horis_book_2)
s.master(codex.de_horis_book_2)

# autumn3
s.inventory_add(codex.bancroft_diaries)
s.master(codex.bancroft_diaries)

# numa12
s.inventory_remove(
    lesson.desires_and_dissolutions,
    lesson.disciplines_of_the_hammer,
    lesson.edicts_liminal,
    lesson.edicts_liminal,
    lesson.pyroglyphics,
    lesson.spices_and_savours,
    lesson.the_great_signs_and_the_great_scars,
    lesson.the_great_signs_and_the_great_scars,
)

# spring3
s.inventory_add(codex.in_the_mountains_as_upon_the_plain_there_may_not_be_a_path_where_none_has_passed)
s.master(codex.in_the_mountains_as_upon_the_plain_there_may_not_be_a_path_where_none_has_passed)

# summer3
s.inventory_add(codex.the_concursum_diaries)
s.master(codex.the_concursum_diaries)

# autumn3
s.inventory_add(codex.the_deeds_of_the_scarred_captain)
s.master(codex.the_deeds_of_the_scarred_captain)

# spring3
s.inventory_add(codex.the_wonderful_shape)
s.master(codex.the_wonderful_shape)

# summer3
s.inventory_add(codex.a_catalogue_of_uncharted_pleasures)
s.master(codex.a_catalogue_of_uncharted_pleasures)

# spring3
s.inventory_add(codex.on_imperfections)
s.master(codex.on_imperfections)

# numa13
s.inventory_remove(
    lesson.glassblowing_and_vesselcrafting,
    lesson.glassblowing_and_vesselcrafting,
    lesson.orchids_and_narcotics,
    lesson.orchids_and_narcotics,
    lesson.path_and_pilgrim,
    lesson.path_and_pilgrim,
    lesson.sharps,
    lesson.sharps,
    lesson.sky_stories,
    lesson.sky_stories,
    lesson.sky_stories,
    lesson.tridesma_hiera,
    lesson.tridesma_hiera,
)

# summer3
s.inventory_add(codex.vinzants_minglings)
s.master(codex.vinzants_minglings)

# autumn3
s.inventory_add(codex.the_lion_and_the_glass)
s.master(codex.the_lion_and_the_glass)

# spring3
s.inventory_add(codex.a_true_and_complete_accounting_of_the_asclepian_mysteries_of_the_roots_of_the_house)
s.master(codex.a_true_and_complete_accounting_of_the_asclepian_mysteries_of_the_roots_of_the_house)

# summer3
s.inventory_add(codex.a_true_history_of_valentine_dewulf)
s.master(codex.a_true_history_of_valentine_dewulf)

# autumn3
s.inventory_add(codex.nix_abolix)
s.master(codex.nix_abolix)

# winter3
s.inventory_add(codex.operations_of_a_certain_finality)
s.master(codex.operations_of_a_certain_finality)

# spring3
s.inventory_add(codex.the_wound_wounds)
s.master(codex.the_wound_wounds)

# autumn3
s.inventory_add(codex.each_flame_his_fuel)
s.master(codex.each_flame_his_fuel)

# winter3
s.inventory_add(codex.the_most_sorrowful_end_of_the_lady_nonna)
s.master(codex.the_most_sorrowful_end_of_the_lady_nonna)

# spring3
s.inventory_add(codex.the_fallen_cross)
s.master(codex.the_fallen_cross)

# numa14
s.inventory_remove(
    lesson.bells_and_brazieries,
    lesson.disciplines_of_the_scar,
    lesson.disciplines_of_the_scar,
    lesson.disciplines_of_the_scar,
    lesson.furs_and_feathers,
    lesson.glaziery_and_lightsmithing,
    lesson.glaziery_and_lightsmithing,
    lesson.glaziery_and_lightsmithing,
    lesson.glaziery_and_lightsmithing,
    lesson.herbs_and_infusions,
    lesson.ouranoscopy,
    lesson.putrefactions_and_calcinations,
    lesson.putrefactions_and_calcinations,
    lesson.weaving_and_knotworking,
    lesson.wolf_stories,
    lesson.wolf_stories,
    lesson.wolf_stories,
)

# summer3
s.inventory_add(codex.the_time_of_division)
s.master(codex.the_time_of_division)

# autumn3
s.inventory_add(codex.wainscot_histories)
s.master(codex.wainscot_histories)

# spring3
s.inventory_add(codex.the_geminiad_ii)
s.master(codex.the_geminiad_ii)

# summer3
s.inventory_add(codex.sunset_celia_and_the_end_of_days)
s.master(codex.sunset_celia_and_the_end_of_days)

# autumn3
s.inventory_add(codex.the_twin_serpent_tantra)
s.master(codex.the_twin_serpent_tantra)

# winter3
s.inventory_add(codex.the_book_of_cinders)
s.master(codex.the_book_of_cinders)

# spring3
s.inventory_add(codex.the_morphy_codex)
s.master(codex.the_morphy_codex)

# autumn3
s.inventory_add(codex.the_viennese_conundra)
s.master(codex.the_viennese_conundra)

# numa15
s.inventory_remove(
    lesson.auroral_contemplations,
    lesson.edicts_liminal,
    lesson.edicts_liminal,
    lesson.pentiments_and_precursors,
    lesson.pentiments_and_precursors,
    lesson.pyroglyphics,
    lesson.sacra_limiae,
    lesson.sacra_limiae,
    lesson.surgeries_and_exsanguinations,
    lesson.surgeries_and_exsanguinations,
    lesson.tridesma_hiera,
    lesson.wolf_stories,
)

# spring3
s.inventory_add(codex.lady_evas_repose)
s.master(codex.lady_evas_repose)

# summer3
s.inventory_add(codex.plantagenet_mysteries)
s.master(codex.plantagenet_mysteries)
s.inventory_remove(liquid.uzult)

# autumn3
s.inventory_add(codex.green_jasper_tablet)
s.master(codex.green_jasper_tablet)

# spring3
s.catalogue(
    codex.echidnalia,
    codex.medusan_commentaries,
    codex.naenian_sketches,
    codex.quirinic_meditations,
    codex.xenodicene_odes,
)
s.master(
    codex.echidnalia,
    codex.medusan_commentaries,
    codex.naenian_sketches,
    codex.quirinic_meditations,
    codex.xenodicene_odes,
)
s.inventory_remove(
    liquid.asimel,
    liquid.marakat,
    liquid.nillycant,
    liquid.perinculate,
)

#############################################################################################################

r.static_available({
    liquid.ichor_auroral: 1,            # cost=1 soul.health_sick(c=+1) skill.sights_and_sensations(p=+9) thing.hurricane_lamp(p=+1) (via shrine_the_chancel)
    memory.ascendant_harmony: 1,        # cost=1 soul.chor_duendratic(c=+1) skill.strings_and_songs(p=+8) tool.mazarine_fife(p=+3) (via desk_nonna)
    memory.beguiling_melody: 1,         # cost=1 soul.health_sick(c=+1) skill.pentiments_and_precursors(p=+3) tool.spice_scales(p=+1) tool.bronze_knife(p=+1) (via altar_ascite)
    memory.bittersweet_certainty: 1,    # cost=1 soul.chor_duendratic(c=+1) skill.ouranoscopy(p=+7) (via shrine_st_januarius)
    memory.cheerful_ditty: 1,           # cost=1 soul.chor_duendratic(c=+1, p=+1) skill.drums_and_dances(p=+9) (via shrine_st_januarius)
    memory.confounding_parable: 1,      # cost=1 soul.health_sick(c=+1) skill.preliminal_meter(p=+8) (via altar_ascite)
    memory.curious_hunch: 2,            # preliminal_meter memory(knock+1)
    memory.earthquake_name: 3,          # cost=3 soul.wist_shell_crossed(c=+1, p=+1) skill.stone_stories(p=+9) tool.serpent_styled_glass(p=+1) memory.old_moment(c=+2, p=+4) (via altar_ascite)
    memory.enduring_reflection: 2,      # cost=2 soul.health_sick(c=+1) skill.path_and_pilgrim(p=+9) memory.the_bells_of_ys(c=+1, p=+5) (via catacombs_altar)
    memory.forbidden_epic: 3,           # cost=3 soul.health_sick(c=+1) skill.edicts_martial(p=+10) memory.confounding_parable(c=+1, p=+2) memory.loopholes(c=+1, p=+5) (via catacombs_altar)
    memory.hives_lament: 1,             # drums_and_dances tool.mazarine_fife tool.bronze_knife (via windlit workbench)
    memory.nameday_riddle: 2,           # fet + solutions_and_separations + any memory
    #memory.old_moment: 2,               # cost=2 soul.health_sick(c=+1) skill.disciplines_of_the_scar(p=+3) comfort.elegant_sunburst_lamp(p=+3) memory.the_paths_of_the_sun(c=+1, p=+5) (via shrine_the_chancel)
    memory.old_moment: 2,               # skill.path_and_pilgrim + fear
    memory.old_wound: 1,                # cost=1 soul.health_sick(c=+1) skill.edicts_martial(p=+10) (via catacombs_altar)
    memory.savage_hymn: 1,              # cost=1 soul.chor_duendratic(c=+1) skill.drums_and_dances(p=+8) (via shrine_st_januarius)
    memory.secret_threshold: 1,         # cost=1 soul.chor_duendratic(c=+1) skill.preliminal_meter(p=+9) (via shrine_st_januarius)
    memory.thunderskins_paean: 1,       # chor + skill.drums_and_dances (via drums)
    memory.torgues_cleansing: 1,        # cost=1 soul.trist_despairing(c=+1, p=+1) skill.auroral_contemplations(p=+9) (via shrine_the_chancel)
    memory.wind_in_waiting: 2,          # cost=2 soul.chor_duendratic(c=+1) skill.strings_and_songs(p=+8) memory.back_into_balance(c=+1, p=+5) tool.mazarine_fife(p=+3) (via desk_nonna)
    memory.winning_move: 2,             # cost=2 soul.health_sick(c=+1) skill.ragged_crossroads(p=+10) memory.merciless_alteration(c=+1, p=+5) (via catacombs_altar)
    memory.wistful_air: 1,              # cost=1 soul.chor_duendratic(c=+1) skill.strings_and_songs(p=+8) (via shrine_st_januarius)
    memory.wormwood_dream: 2,           # cost=2 soul.health_sick(c=+1) skill.edicts_martial(p=+10) memory.loopholes(c=+1, p=+5) (via catacombs_altar)
})

s.inventory_add(
    #weather.clouds,
    #weather.fog,
    #weather.gale,
    #weather.hail,
    #weather.nume_brume,
    #weather.rain,
    #weather.snow,
    #weather.storm,
    #weather.sunny,                     # (lantern, sky)

    #memory.a_final_understanding,      # n. 1   (rose, sky, winter)     (towards_a_fundamental_aesthetic_second_edition + ericapaean)
    #memory.a_stolen_secret,            # .. 1   (knock, moon)           (knock8 the_gospel_of_zacchaeus)
    #memory.an_irresistible_feast,      # n. 1   (edge, grail, nectar)   (thing.the_writing_on_the_wall + vak)
    #memory.ascendant_harmony,          # pc 1.5 (lantern, sky)
    #memory.back_into_balance,          # n. 1   (heart, sky, winter)    (codex.the_sky_in_the_scar + sabazine)
    #memory.beguiling_melody,           # .c 1   (grail, sky)            (grail4 the_winds_ruin)
    #memory.bittersweet_certainty,      # .c 1   (lantern, winter)       (winter8 musgraves_sketches) (SKOR LANTERN)
    #memory.cheerful_ditty,             # .c 1   (heart, sky)            (sky4 perugian_diaries) (SKOR HEART)
    #memory.confounding_parable,        # .c 1   (moon, rose, sky)       (rose6 letters_from_a_fugitive)
    #memory.contradiction,              # .. 1   (edge, moon)            (edge4 the_victory_of_crowns)
    #memory.curious_hunch,              # pc 1.5 (heart, knock, lantern, moth)
    #memory.didumos,                    # pc 2   (knock, lantern, sky, winter)
    #memory.earth_sign,                 # p. x   (nectar, scale)
    #memory.earthquake_name,            # pc 2   (forge, scale)
    #memory.enduring_reflection,        # pc 1.5 (heart, knock, rose)
    #memory.fear,                       # .. 0.5 (edge, scale)           (scale6 the_encircling_tantra)
    #memory.forbidden_epic,             # pc 2   (edge, moon, rose)
    #memory.foresight,                  # .. 1   (forge, lantern)        (forge6 the_vinzant_inscriptions)
    #memory.gossip,                     # .. 1   (grail, rose)           (nectar4 three_flowers_hath_the_tree)
    #memory.hindsight,                  # .. 1   (scale, winter)         (winter6 oblations_in_iron)
    #memory.hives_lament,               # pc 1.5 (moth, nectar, winter)
    #memory.horizon_sight,              # pc 2   (rose)
    #memory.impulse,                    # .. 0.2 (moth, nectar)          (nectar6 the_shadow_in_the_stair)
    #memory.inescapable_confinement,    # n. 1   (knock, scale, winter)  (towards_a_fundamental_aesthetic + ericapeaen)
    #memory.intuition,                  # .. 1   (moon, rose)            (rose6 the_book_of_the_centipede)
    #memory.invincible_audacity,        # pc 2   (edge, forge, latern)
    #memory.loopholes,                  # n. 1   (knock, moon, moth)     (tablet.serpent_root + cracktrack)
    #memory.loss,                       # .. 0.2 (edge, winter)
    #memory.merciless_alteration,       # n. 1   (edge, forge, grail)    (a_childs_treasury_of_golden_afternoons + hyksos)
    #memory.nameday_riddle,             # .c 1.5 (knock, moth)
    #memory.occult_scrap,               # p. 1   (knock, moth, rose)
    #memory.old_moment,                 # .c 1.5 (lantern, moth, scale)
    #memory.old_wound,                  # pc 1   (edge, moon, winter)
    #memory.pattern,                    # .. 1   (forge, knock)          (knock4 advice_on_containment)
    #memory.regret,                     # .. 1   (forge, winter)         (winter4 annals_of_st_brandans)
    #memory.revelation,                 # .. 1   (lantern)               (lantern4 the_locksmiths_dream_a_light_through_the_keyhole)
    #memory.salt,                       # .. 1   (knock, moon, winter)   (moon6 the_sea_does_not_regret)
    #memory.satisfaction,               # .. 0.2 (grail, heart)          (grail6 an_impertinent_vitulation)
    #memory.savage_hymn,                # .c 1   (scale, sky)            (scale6 singlefoot_songs)
    #memory.scent,                      # .. 0.5 (nectar)
    #memory.secret_threshold,           # .c 1   (knock, rose)           (forge10 the_temptations_of_architecture) (SKOR KNOCK)
    #memory.sight,                      # .. 0.5 (lantern)
    #memory.solace,                     # .. 1   (heart, sky)            (sky6 travelling_at_night_vol_2)
    #memory.sound,                      # .. 0.5 (heart)
    #memory.storm,                      # ..  1  (heart, sky)            (sky10 de_motu_corporum_vetitorum)
    #memory.taste,                      # .. 0.5 (grail)
    #memory.that_old_lost_music,        # n. 1   (rose, scale, sky)      (the_turquoise_hand + ramsund)
    #memory.the_bells_of_ys,            # n. 1   (edge, forge, rose)     (tablet.amiranis_beteli + fucine)
    #memory.the_great_counterfeit,      # n. 1   (lantern, moon, nectar) (scroll.shuritic_book_of_suns + mandaic)
    #memory.the_paths_of_the_sun,       # n. 1   (forge, knock, lantern) (tablet.the_suns_design + cracktrack)
    #memory.the_suns_weakness,          # n. 1   (grail, lantern, moth)  (scroll.the_sun_disfigured + cracktrack)
    #memory.three_rules,                # n. 1   (heart, moth, scale)    (the_three_and_the_three_st_chiavi_manuscript)
    #memory.thunderskins_paean,         # .c 1.5 (grail, heart, scale)
    #memory.torgues_cleansing,          # .c 1   (edge)
    #memory.touch,                      # .. 0.5 (forge)
    #memory.weaving_the_world,          # n. 1   (heart, moon, nectar)   (tablet.kopralith_omphalos + killasimi)
    #memory.wild_surmise,               # .. 0.5 (lantern, moth, sky)
    #memory.wind_in_waiting,            # pc 2   (grail, moth, scale, sky)
    #memory.winning_move,               # .c 1.5 (edge)
    #memory.wistful_air,                # .c 1   (rose, sky)
    #memory.wormwood_dream,             # pc 1.5 (edge, moon, winter)

    #assistance.barber,
    #assistance.blacksmith,
    #assistance.coffinmaker,
    #assistance.fisherman,
    #assistance.midwife,
    #assistance.miner,
    #assistance.nun,
    #assistance.orchard_keeper,
    assistance.rector,
)

s.next_opportunities(
    #"art_its_educational",
    #"comfort_relevant_furniture",
    #"extra_effort_soul",
    #"only_connect_memory",
    #"stuff_also_things",
    #"the_right_skies_weather",

    #"awen",     # knock2, lantern2, rose2, sky2
    #"duende",   # grail2, heart2, nectar2
    #"epiphany", # forge2, moon2, moth2
    #"ubi_sunt", # edge2, scale2, winter2
)

#s.inventory_remove_soul(soul.fet, level=1)

#r.print_inventory_costs()
#r.print_inventory_counts()
r.print_static_available()
r.print_available_card_solutions()
r.print_room_unlock_solutions()
r.print_item_unlock_solutions()
r.print_recipe_solutions()
r.print_skill_upgrade_solutions()
r.print_evolving_solutions()
