from api.models.talent import Talent
from .a_talent_seeds import talent_seeds_a
from .b_talent_seeds import talent_seeds_b
from .c_talent_seeds import talent_seeds_c
from .d_talent_seeds import talent_seeds_d
from .e_talent_seeds import talent_seeds_e
from .f_talent_seeds import talent_seeds_f
from .g_talent_seeds import talent_seeds_g
from .h_talent_seeds import talent_seeds_h
from .i_talent_seeds import talent_seeds_i
from .k_talent_seeds import talent_seeds_k
from .l_talent_seeds import talent_seeds_l
from .m_talent_seeds import talent_seeds_m
from .o_talent_seeds import talent_seeds_o
from .p_talent_seeds import talent_seeds_p
from .r_talent_seeds import talent_seeds_r
from .s_talent_seeds import talent_seeds_s
from .t_talent_seeds import talent_seeds_t
from .u_talent_seeds import talent_seeds_u
from .v_talent_seeds import talent_seeds_v
from .w_talent_seeds import talent_seeds_w

talent_seeds = talent_seeds_a + talent_seeds_b + talent_seeds_c + talent_seeds_d + talent_seeds_e + talent_seeds_f + talent_seeds_g + talent_seeds_h + talent_seeds_i + talent_seeds_k + talent_seeds_l + talent_seeds_m + talent_seeds_o + talent_seeds_p + talent_seeds_r + talent_seeds_s + talent_seeds_t + talent_seeds_u + talent_seeds_v + talent_seeds_w


def seed_talents():
    """Seeds Talents if Talent Id is not found"""
    for talent_seed in talent_seeds:
        if Talent.find_by_id(talent_seed["id"]) is None:
            saved_talent = Talent(**talent_seed).save()
            print("{0} talent saved".format(saved_talent.name))
        else:
            print("{0} talent found".format(talent_seed["id"]))
