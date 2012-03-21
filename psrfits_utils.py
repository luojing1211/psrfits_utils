# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.3
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_psrfits_utils', [dirname(__file__)])
        except ImportError:
            import _psrfits_utils
            return _psrfits_utils
        if fp is not None:
            try:
                _mod = imp.load_module('_psrfits_utils', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _psrfits_utils = swig_import_helper()
    del swig_import_helper
else:
    import _psrfits_utils
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0



def malloc_floatp(*args):
  return _psrfits_utils.malloc_floatp(*args)
malloc_floatp = _psrfits_utils.malloc_floatp

def free_floatp(*args):
  return _psrfits_utils.free_floatp(*args)
free_floatp = _psrfits_utils.free_floatp

def malloc_ucharp(*args):
  return _psrfits_utils.malloc_ucharp(*args)
malloc_ucharp = _psrfits_utils.malloc_ucharp

def free_ucharp(*args):
  return _psrfits_utils.free_ucharp(*args)
free_ucharp = _psrfits_utils.free_ucharp
PSRFITS_MAXFILELEN_SEARCH = _psrfits_utils.PSRFITS_MAXFILELEN_SEARCH
PSRFITS_MAXFILELEN_FOLD = _psrfits_utils.PSRFITS_MAXFILELEN_FOLD
PSRFITS_SEARCH_TEMPLATE = _psrfits_utils.PSRFITS_SEARCH_TEMPLATE
PSRFITS_FOLD_TEMPLATE = _psrfits_utils.PSRFITS_FOLD_TEMPLATE
class hdrinfo(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, hdrinfo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, hdrinfo, name)
    __repr__ = _swig_repr
    __swig_setmethods__["obs_mode"] = _psrfits_utils.hdrinfo_obs_mode_set
    __swig_getmethods__["obs_mode"] = _psrfits_utils.hdrinfo_obs_mode_get
    if _newclass:obs_mode = _swig_property(_psrfits_utils.hdrinfo_obs_mode_get, _psrfits_utils.hdrinfo_obs_mode_set)
    __swig_setmethods__["telescope"] = _psrfits_utils.hdrinfo_telescope_set
    __swig_getmethods__["telescope"] = _psrfits_utils.hdrinfo_telescope_get
    if _newclass:telescope = _swig_property(_psrfits_utils.hdrinfo_telescope_get, _psrfits_utils.hdrinfo_telescope_set)
    __swig_setmethods__["observer"] = _psrfits_utils.hdrinfo_observer_set
    __swig_getmethods__["observer"] = _psrfits_utils.hdrinfo_observer_get
    if _newclass:observer = _swig_property(_psrfits_utils.hdrinfo_observer_get, _psrfits_utils.hdrinfo_observer_set)
    __swig_setmethods__["source"] = _psrfits_utils.hdrinfo_source_set
    __swig_getmethods__["source"] = _psrfits_utils.hdrinfo_source_get
    if _newclass:source = _swig_property(_psrfits_utils.hdrinfo_source_get, _psrfits_utils.hdrinfo_source_set)
    __swig_setmethods__["frontend"] = _psrfits_utils.hdrinfo_frontend_set
    __swig_getmethods__["frontend"] = _psrfits_utils.hdrinfo_frontend_get
    if _newclass:frontend = _swig_property(_psrfits_utils.hdrinfo_frontend_get, _psrfits_utils.hdrinfo_frontend_set)
    __swig_setmethods__["backend"] = _psrfits_utils.hdrinfo_backend_set
    __swig_getmethods__["backend"] = _psrfits_utils.hdrinfo_backend_get
    if _newclass:backend = _swig_property(_psrfits_utils.hdrinfo_backend_get, _psrfits_utils.hdrinfo_backend_set)
    __swig_setmethods__["project_id"] = _psrfits_utils.hdrinfo_project_id_set
    __swig_getmethods__["project_id"] = _psrfits_utils.hdrinfo_project_id_get
    if _newclass:project_id = _swig_property(_psrfits_utils.hdrinfo_project_id_get, _psrfits_utils.hdrinfo_project_id_set)
    __swig_setmethods__["date_obs"] = _psrfits_utils.hdrinfo_date_obs_set
    __swig_getmethods__["date_obs"] = _psrfits_utils.hdrinfo_date_obs_get
    if _newclass:date_obs = _swig_property(_psrfits_utils.hdrinfo_date_obs_get, _psrfits_utils.hdrinfo_date_obs_set)
    __swig_setmethods__["ra_str"] = _psrfits_utils.hdrinfo_ra_str_set
    __swig_getmethods__["ra_str"] = _psrfits_utils.hdrinfo_ra_str_get
    if _newclass:ra_str = _swig_property(_psrfits_utils.hdrinfo_ra_str_get, _psrfits_utils.hdrinfo_ra_str_set)
    __swig_setmethods__["dec_str"] = _psrfits_utils.hdrinfo_dec_str_set
    __swig_getmethods__["dec_str"] = _psrfits_utils.hdrinfo_dec_str_get
    if _newclass:dec_str = _swig_property(_psrfits_utils.hdrinfo_dec_str_get, _psrfits_utils.hdrinfo_dec_str_set)
    __swig_setmethods__["poln_type"] = _psrfits_utils.hdrinfo_poln_type_set
    __swig_getmethods__["poln_type"] = _psrfits_utils.hdrinfo_poln_type_get
    if _newclass:poln_type = _swig_property(_psrfits_utils.hdrinfo_poln_type_get, _psrfits_utils.hdrinfo_poln_type_set)
    __swig_setmethods__["poln_order"] = _psrfits_utils.hdrinfo_poln_order_set
    __swig_getmethods__["poln_order"] = _psrfits_utils.hdrinfo_poln_order_get
    if _newclass:poln_order = _swig_property(_psrfits_utils.hdrinfo_poln_order_get, _psrfits_utils.hdrinfo_poln_order_set)
    __swig_setmethods__["track_mode"] = _psrfits_utils.hdrinfo_track_mode_set
    __swig_getmethods__["track_mode"] = _psrfits_utils.hdrinfo_track_mode_get
    if _newclass:track_mode = _swig_property(_psrfits_utils.hdrinfo_track_mode_get, _psrfits_utils.hdrinfo_track_mode_set)
    __swig_setmethods__["cal_mode"] = _psrfits_utils.hdrinfo_cal_mode_set
    __swig_getmethods__["cal_mode"] = _psrfits_utils.hdrinfo_cal_mode_get
    if _newclass:cal_mode = _swig_property(_psrfits_utils.hdrinfo_cal_mode_get, _psrfits_utils.hdrinfo_cal_mode_set)
    __swig_setmethods__["feed_mode"] = _psrfits_utils.hdrinfo_feed_mode_set
    __swig_getmethods__["feed_mode"] = _psrfits_utils.hdrinfo_feed_mode_get
    if _newclass:feed_mode = _swig_property(_psrfits_utils.hdrinfo_feed_mode_get, _psrfits_utils.hdrinfo_feed_mode_set)
    __swig_setmethods__["MJD_epoch"] = _psrfits_utils.hdrinfo_MJD_epoch_set
    __swig_getmethods__["MJD_epoch"] = _psrfits_utils.hdrinfo_MJD_epoch_get
    if _newclass:MJD_epoch = _swig_property(_psrfits_utils.hdrinfo_MJD_epoch_get, _psrfits_utils.hdrinfo_MJD_epoch_set)
    __swig_setmethods__["dt"] = _psrfits_utils.hdrinfo_dt_set
    __swig_getmethods__["dt"] = _psrfits_utils.hdrinfo_dt_get
    if _newclass:dt = _swig_property(_psrfits_utils.hdrinfo_dt_get, _psrfits_utils.hdrinfo_dt_set)
    __swig_setmethods__["fctr"] = _psrfits_utils.hdrinfo_fctr_set
    __swig_getmethods__["fctr"] = _psrfits_utils.hdrinfo_fctr_get
    if _newclass:fctr = _swig_property(_psrfits_utils.hdrinfo_fctr_get, _psrfits_utils.hdrinfo_fctr_set)
    __swig_setmethods__["orig_df"] = _psrfits_utils.hdrinfo_orig_df_set
    __swig_getmethods__["orig_df"] = _psrfits_utils.hdrinfo_orig_df_get
    if _newclass:orig_df = _swig_property(_psrfits_utils.hdrinfo_orig_df_get, _psrfits_utils.hdrinfo_orig_df_set)
    __swig_setmethods__["df"] = _psrfits_utils.hdrinfo_df_set
    __swig_getmethods__["df"] = _psrfits_utils.hdrinfo_df_get
    if _newclass:df = _swig_property(_psrfits_utils.hdrinfo_df_get, _psrfits_utils.hdrinfo_df_set)
    __swig_setmethods__["BW"] = _psrfits_utils.hdrinfo_BW_set
    __swig_getmethods__["BW"] = _psrfits_utils.hdrinfo_BW_get
    if _newclass:BW = _swig_property(_psrfits_utils.hdrinfo_BW_get, _psrfits_utils.hdrinfo_BW_set)
    __swig_setmethods__["ra2000"] = _psrfits_utils.hdrinfo_ra2000_set
    __swig_getmethods__["ra2000"] = _psrfits_utils.hdrinfo_ra2000_get
    if _newclass:ra2000 = _swig_property(_psrfits_utils.hdrinfo_ra2000_get, _psrfits_utils.hdrinfo_ra2000_set)
    __swig_setmethods__["dec2000"] = _psrfits_utils.hdrinfo_dec2000_set
    __swig_getmethods__["dec2000"] = _psrfits_utils.hdrinfo_dec2000_get
    if _newclass:dec2000 = _swig_property(_psrfits_utils.hdrinfo_dec2000_get, _psrfits_utils.hdrinfo_dec2000_set)
    __swig_setmethods__["azimuth"] = _psrfits_utils.hdrinfo_azimuth_set
    __swig_getmethods__["azimuth"] = _psrfits_utils.hdrinfo_azimuth_get
    if _newclass:azimuth = _swig_property(_psrfits_utils.hdrinfo_azimuth_get, _psrfits_utils.hdrinfo_azimuth_set)
    __swig_setmethods__["zenith_ang"] = _psrfits_utils.hdrinfo_zenith_ang_set
    __swig_getmethods__["zenith_ang"] = _psrfits_utils.hdrinfo_zenith_ang_get
    if _newclass:zenith_ang = _swig_property(_psrfits_utils.hdrinfo_zenith_ang_get, _psrfits_utils.hdrinfo_zenith_ang_set)
    __swig_setmethods__["beam_FWHM"] = _psrfits_utils.hdrinfo_beam_FWHM_set
    __swig_getmethods__["beam_FWHM"] = _psrfits_utils.hdrinfo_beam_FWHM_get
    if _newclass:beam_FWHM = _swig_property(_psrfits_utils.hdrinfo_beam_FWHM_get, _psrfits_utils.hdrinfo_beam_FWHM_set)
    __swig_setmethods__["cal_freq"] = _psrfits_utils.hdrinfo_cal_freq_set
    __swig_getmethods__["cal_freq"] = _psrfits_utils.hdrinfo_cal_freq_get
    if _newclass:cal_freq = _swig_property(_psrfits_utils.hdrinfo_cal_freq_get, _psrfits_utils.hdrinfo_cal_freq_set)
    __swig_setmethods__["cal_dcyc"] = _psrfits_utils.hdrinfo_cal_dcyc_set
    __swig_getmethods__["cal_dcyc"] = _psrfits_utils.hdrinfo_cal_dcyc_get
    if _newclass:cal_dcyc = _swig_property(_psrfits_utils.hdrinfo_cal_dcyc_get, _psrfits_utils.hdrinfo_cal_dcyc_set)
    __swig_setmethods__["cal_phs"] = _psrfits_utils.hdrinfo_cal_phs_set
    __swig_getmethods__["cal_phs"] = _psrfits_utils.hdrinfo_cal_phs_get
    if _newclass:cal_phs = _swig_property(_psrfits_utils.hdrinfo_cal_phs_get, _psrfits_utils.hdrinfo_cal_phs_set)
    __swig_setmethods__["feed_angle"] = _psrfits_utils.hdrinfo_feed_angle_set
    __swig_getmethods__["feed_angle"] = _psrfits_utils.hdrinfo_feed_angle_get
    if _newclass:feed_angle = _swig_property(_psrfits_utils.hdrinfo_feed_angle_get, _psrfits_utils.hdrinfo_feed_angle_set)
    __swig_setmethods__["scanlen"] = _psrfits_utils.hdrinfo_scanlen_set
    __swig_getmethods__["scanlen"] = _psrfits_utils.hdrinfo_scanlen_get
    if _newclass:scanlen = _swig_property(_psrfits_utils.hdrinfo_scanlen_get, _psrfits_utils.hdrinfo_scanlen_set)
    __swig_setmethods__["start_lst"] = _psrfits_utils.hdrinfo_start_lst_set
    __swig_getmethods__["start_lst"] = _psrfits_utils.hdrinfo_start_lst_get
    if _newclass:start_lst = _swig_property(_psrfits_utils.hdrinfo_start_lst_get, _psrfits_utils.hdrinfo_start_lst_set)
    __swig_setmethods__["start_sec"] = _psrfits_utils.hdrinfo_start_sec_set
    __swig_getmethods__["start_sec"] = _psrfits_utils.hdrinfo_start_sec_get
    if _newclass:start_sec = _swig_property(_psrfits_utils.hdrinfo_start_sec_get, _psrfits_utils.hdrinfo_start_sec_set)
    __swig_setmethods__["chan_dm"] = _psrfits_utils.hdrinfo_chan_dm_set
    __swig_getmethods__["chan_dm"] = _psrfits_utils.hdrinfo_chan_dm_get
    if _newclass:chan_dm = _swig_property(_psrfits_utils.hdrinfo_chan_dm_get, _psrfits_utils.hdrinfo_chan_dm_set)
    __swig_setmethods__["fd_sang"] = _psrfits_utils.hdrinfo_fd_sang_set
    __swig_getmethods__["fd_sang"] = _psrfits_utils.hdrinfo_fd_sang_get
    if _newclass:fd_sang = _swig_property(_psrfits_utils.hdrinfo_fd_sang_get, _psrfits_utils.hdrinfo_fd_sang_set)
    __swig_setmethods__["fd_xyph"] = _psrfits_utils.hdrinfo_fd_xyph_set
    __swig_getmethods__["fd_xyph"] = _psrfits_utils.hdrinfo_fd_xyph_get
    if _newclass:fd_xyph = _swig_property(_psrfits_utils.hdrinfo_fd_xyph_get, _psrfits_utils.hdrinfo_fd_xyph_set)
    __swig_setmethods__["start_day"] = _psrfits_utils.hdrinfo_start_day_set
    __swig_getmethods__["start_day"] = _psrfits_utils.hdrinfo_start_day_get
    if _newclass:start_day = _swig_property(_psrfits_utils.hdrinfo_start_day_get, _psrfits_utils.hdrinfo_start_day_set)
    __swig_setmethods__["scan_number"] = _psrfits_utils.hdrinfo_scan_number_set
    __swig_getmethods__["scan_number"] = _psrfits_utils.hdrinfo_scan_number_get
    if _newclass:scan_number = _swig_property(_psrfits_utils.hdrinfo_scan_number_get, _psrfits_utils.hdrinfo_scan_number_set)
    __swig_setmethods__["nbits"] = _psrfits_utils.hdrinfo_nbits_set
    __swig_getmethods__["nbits"] = _psrfits_utils.hdrinfo_nbits_get
    if _newclass:nbits = _swig_property(_psrfits_utils.hdrinfo_nbits_get, _psrfits_utils.hdrinfo_nbits_set)
    __swig_setmethods__["nbin"] = _psrfits_utils.hdrinfo_nbin_set
    __swig_getmethods__["nbin"] = _psrfits_utils.hdrinfo_nbin_get
    if _newclass:nbin = _swig_property(_psrfits_utils.hdrinfo_nbin_get, _psrfits_utils.hdrinfo_nbin_set)
    __swig_setmethods__["nchan"] = _psrfits_utils.hdrinfo_nchan_set
    __swig_getmethods__["nchan"] = _psrfits_utils.hdrinfo_nchan_get
    if _newclass:nchan = _swig_property(_psrfits_utils.hdrinfo_nchan_get, _psrfits_utils.hdrinfo_nchan_set)
    __swig_setmethods__["npol"] = _psrfits_utils.hdrinfo_npol_set
    __swig_getmethods__["npol"] = _psrfits_utils.hdrinfo_npol_get
    if _newclass:npol = _swig_property(_psrfits_utils.hdrinfo_npol_get, _psrfits_utils.hdrinfo_npol_set)
    __swig_setmethods__["nsblk"] = _psrfits_utils.hdrinfo_nsblk_set
    __swig_getmethods__["nsblk"] = _psrfits_utils.hdrinfo_nsblk_get
    if _newclass:nsblk = _swig_property(_psrfits_utils.hdrinfo_nsblk_get, _psrfits_utils.hdrinfo_nsblk_set)
    __swig_setmethods__["orig_nchan"] = _psrfits_utils.hdrinfo_orig_nchan_set
    __swig_getmethods__["orig_nchan"] = _psrfits_utils.hdrinfo_orig_nchan_get
    if _newclass:orig_nchan = _swig_property(_psrfits_utils.hdrinfo_orig_nchan_get, _psrfits_utils.hdrinfo_orig_nchan_set)
    __swig_setmethods__["summed_polns"] = _psrfits_utils.hdrinfo_summed_polns_set
    __swig_getmethods__["summed_polns"] = _psrfits_utils.hdrinfo_summed_polns_get
    if _newclass:summed_polns = _swig_property(_psrfits_utils.hdrinfo_summed_polns_get, _psrfits_utils.hdrinfo_summed_polns_set)
    __swig_setmethods__["rcvr_polns"] = _psrfits_utils.hdrinfo_rcvr_polns_set
    __swig_getmethods__["rcvr_polns"] = _psrfits_utils.hdrinfo_rcvr_polns_get
    if _newclass:rcvr_polns = _swig_property(_psrfits_utils.hdrinfo_rcvr_polns_get, _psrfits_utils.hdrinfo_rcvr_polns_set)
    __swig_setmethods__["offset_subint"] = _psrfits_utils.hdrinfo_offset_subint_set
    __swig_getmethods__["offset_subint"] = _psrfits_utils.hdrinfo_offset_subint_get
    if _newclass:offset_subint = _swig_property(_psrfits_utils.hdrinfo_offset_subint_get, _psrfits_utils.hdrinfo_offset_subint_set)
    __swig_setmethods__["ds_time_fact"] = _psrfits_utils.hdrinfo_ds_time_fact_set
    __swig_getmethods__["ds_time_fact"] = _psrfits_utils.hdrinfo_ds_time_fact_get
    if _newclass:ds_time_fact = _swig_property(_psrfits_utils.hdrinfo_ds_time_fact_get, _psrfits_utils.hdrinfo_ds_time_fact_set)
    __swig_setmethods__["ds_freq_fact"] = _psrfits_utils.hdrinfo_ds_freq_fact_set
    __swig_getmethods__["ds_freq_fact"] = _psrfits_utils.hdrinfo_ds_freq_fact_get
    if _newclass:ds_freq_fact = _swig_property(_psrfits_utils.hdrinfo_ds_freq_fact_get, _psrfits_utils.hdrinfo_ds_freq_fact_set)
    __swig_setmethods__["onlyI"] = _psrfits_utils.hdrinfo_onlyI_set
    __swig_getmethods__["onlyI"] = _psrfits_utils.hdrinfo_onlyI_get
    if _newclass:onlyI = _swig_property(_psrfits_utils.hdrinfo_onlyI_get, _psrfits_utils.hdrinfo_onlyI_set)
    __swig_setmethods__["fd_hand"] = _psrfits_utils.hdrinfo_fd_hand_set
    __swig_getmethods__["fd_hand"] = _psrfits_utils.hdrinfo_fd_hand_get
    if _newclass:fd_hand = _swig_property(_psrfits_utils.hdrinfo_fd_hand_get, _psrfits_utils.hdrinfo_fd_hand_set)
    __swig_setmethods__["be_phase"] = _psrfits_utils.hdrinfo_be_phase_set
    __swig_getmethods__["be_phase"] = _psrfits_utils.hdrinfo_be_phase_get
    if _newclass:be_phase = _swig_property(_psrfits_utils.hdrinfo_be_phase_get, _psrfits_utils.hdrinfo_be_phase_set)
    def __init__(self): 
        this = _psrfits_utils.new_hdrinfo()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _psrfits_utils.delete_hdrinfo
    __del__ = lambda self : None;
hdrinfo_swigregister = _psrfits_utils.hdrinfo_swigregister
hdrinfo_swigregister(hdrinfo)

class subint(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, subint, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, subint, name)
    __repr__ = _swig_repr
    __swig_setmethods__["tsubint"] = _psrfits_utils.subint_tsubint_set
    __swig_getmethods__["tsubint"] = _psrfits_utils.subint_tsubint_get
    if _newclass:tsubint = _swig_property(_psrfits_utils.subint_tsubint_get, _psrfits_utils.subint_tsubint_set)
    __swig_setmethods__["offs"] = _psrfits_utils.subint_offs_set
    __swig_getmethods__["offs"] = _psrfits_utils.subint_offs_get
    if _newclass:offs = _swig_property(_psrfits_utils.subint_offs_get, _psrfits_utils.subint_offs_set)
    __swig_setmethods__["lst"] = _psrfits_utils.subint_lst_set
    __swig_getmethods__["lst"] = _psrfits_utils.subint_lst_get
    if _newclass:lst = _swig_property(_psrfits_utils.subint_lst_get, _psrfits_utils.subint_lst_set)
    __swig_setmethods__["ra"] = _psrfits_utils.subint_ra_set
    __swig_getmethods__["ra"] = _psrfits_utils.subint_ra_get
    if _newclass:ra = _swig_property(_psrfits_utils.subint_ra_get, _psrfits_utils.subint_ra_set)
    __swig_setmethods__["dec"] = _psrfits_utils.subint_dec_set
    __swig_getmethods__["dec"] = _psrfits_utils.subint_dec_get
    if _newclass:dec = _swig_property(_psrfits_utils.subint_dec_get, _psrfits_utils.subint_dec_set)
    __swig_setmethods__["glon"] = _psrfits_utils.subint_glon_set
    __swig_getmethods__["glon"] = _psrfits_utils.subint_glon_get
    if _newclass:glon = _swig_property(_psrfits_utils.subint_glon_get, _psrfits_utils.subint_glon_set)
    __swig_setmethods__["glat"] = _psrfits_utils.subint_glat_set
    __swig_getmethods__["glat"] = _psrfits_utils.subint_glat_get
    if _newclass:glat = _swig_property(_psrfits_utils.subint_glat_get, _psrfits_utils.subint_glat_set)
    __swig_setmethods__["feed_ang"] = _psrfits_utils.subint_feed_ang_set
    __swig_getmethods__["feed_ang"] = _psrfits_utils.subint_feed_ang_get
    if _newclass:feed_ang = _swig_property(_psrfits_utils.subint_feed_ang_get, _psrfits_utils.subint_feed_ang_set)
    __swig_setmethods__["pos_ang"] = _psrfits_utils.subint_pos_ang_set
    __swig_getmethods__["pos_ang"] = _psrfits_utils.subint_pos_ang_get
    if _newclass:pos_ang = _swig_property(_psrfits_utils.subint_pos_ang_get, _psrfits_utils.subint_pos_ang_set)
    __swig_setmethods__["par_ang"] = _psrfits_utils.subint_par_ang_set
    __swig_getmethods__["par_ang"] = _psrfits_utils.subint_par_ang_get
    if _newclass:par_ang = _swig_property(_psrfits_utils.subint_par_ang_get, _psrfits_utils.subint_par_ang_set)
    __swig_setmethods__["tel_az"] = _psrfits_utils.subint_tel_az_set
    __swig_getmethods__["tel_az"] = _psrfits_utils.subint_tel_az_get
    if _newclass:tel_az = _swig_property(_psrfits_utils.subint_tel_az_get, _psrfits_utils.subint_tel_az_set)
    __swig_setmethods__["tel_zen"] = _psrfits_utils.subint_tel_zen_set
    __swig_getmethods__["tel_zen"] = _psrfits_utils.subint_tel_zen_get
    if _newclass:tel_zen = _swig_property(_psrfits_utils.subint_tel_zen_get, _psrfits_utils.subint_tel_zen_set)
    __swig_setmethods__["bytes_per_subint"] = _psrfits_utils.subint_bytes_per_subint_set
    __swig_getmethods__["bytes_per_subint"] = _psrfits_utils.subint_bytes_per_subint_get
    if _newclass:bytes_per_subint = _swig_property(_psrfits_utils.subint_bytes_per_subint_get, _psrfits_utils.subint_bytes_per_subint_set)
    __swig_setmethods__["FITS_typecode"] = _psrfits_utils.subint_FITS_typecode_set
    __swig_getmethods__["FITS_typecode"] = _psrfits_utils.subint_FITS_typecode_get
    if _newclass:FITS_typecode = _swig_property(_psrfits_utils.subint_FITS_typecode_get, _psrfits_utils.subint_FITS_typecode_set)
    __swig_setmethods__["dat_freqs"] = _psrfits_utils.subint_dat_freqs_set
    __swig_getmethods__["dat_freqs"] = _psrfits_utils.subint_dat_freqs_get
    if _newclass:dat_freqs = _swig_property(_psrfits_utils.subint_dat_freqs_get, _psrfits_utils.subint_dat_freqs_set)
    __swig_setmethods__["dat_weights"] = _psrfits_utils.subint_dat_weights_set
    __swig_getmethods__["dat_weights"] = _psrfits_utils.subint_dat_weights_get
    if _newclass:dat_weights = _swig_property(_psrfits_utils.subint_dat_weights_get, _psrfits_utils.subint_dat_weights_set)
    __swig_setmethods__["dat_offsets"] = _psrfits_utils.subint_dat_offsets_set
    __swig_getmethods__["dat_offsets"] = _psrfits_utils.subint_dat_offsets_get
    if _newclass:dat_offsets = _swig_property(_psrfits_utils.subint_dat_offsets_get, _psrfits_utils.subint_dat_offsets_set)
    __swig_setmethods__["dat_scales"] = _psrfits_utils.subint_dat_scales_set
    __swig_getmethods__["dat_scales"] = _psrfits_utils.subint_dat_scales_get
    if _newclass:dat_scales = _swig_property(_psrfits_utils.subint_dat_scales_get, _psrfits_utils.subint_dat_scales_set)
    __swig_setmethods__["fdata"] = _psrfits_utils.subint_fdata_set
    __swig_getmethods__["fdata"] = _psrfits_utils.subint_fdata_get
    if _newclass:fdata = _swig_property(_psrfits_utils.subint_fdata_get, _psrfits_utils.subint_fdata_set)
    __swig_setmethods__["rawdata"] = _psrfits_utils.subint_rawdata_set
    __swig_getmethods__["rawdata"] = _psrfits_utils.subint_rawdata_get
    if _newclass:rawdata = _swig_property(_psrfits_utils.subint_rawdata_get, _psrfits_utils.subint_rawdata_set)
    __swig_setmethods__["data"] = _psrfits_utils.subint_data_set
    __swig_getmethods__["data"] = _psrfits_utils.subint_data_get
    if _newclass:data = _swig_property(_psrfits_utils.subint_data_get, _psrfits_utils.subint_data_set)
    def __init__(self): 
        this = _psrfits_utils.new_subint()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _psrfits_utils.delete_subint
    __del__ = lambda self : None;
subint_swigregister = _psrfits_utils.subint_swigregister
subint_swigregister(subint)

class foldinfo(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, foldinfo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, foldinfo, name)
    __repr__ = _swig_repr
    __swig_setmethods__["parfile"] = _psrfits_utils.foldinfo_parfile_set
    __swig_getmethods__["parfile"] = _psrfits_utils.foldinfo_parfile_get
    if _newclass:parfile = _swig_property(_psrfits_utils.foldinfo_parfile_get, _psrfits_utils.foldinfo_parfile_set)
    __swig_setmethods__["n_polyco_sets"] = _psrfits_utils.foldinfo_n_polyco_sets_set
    __swig_getmethods__["n_polyco_sets"] = _psrfits_utils.foldinfo_n_polyco_sets_get
    if _newclass:n_polyco_sets = _swig_property(_psrfits_utils.foldinfo_n_polyco_sets_get, _psrfits_utils.foldinfo_n_polyco_sets_set)
    __swig_setmethods__["pc"] = _psrfits_utils.foldinfo_pc_set
    __swig_getmethods__["pc"] = _psrfits_utils.foldinfo_pc_get
    if _newclass:pc = _swig_property(_psrfits_utils.foldinfo_pc_get, _psrfits_utils.foldinfo_pc_set)
    __swig_setmethods__["nbin"] = _psrfits_utils.foldinfo_nbin_set
    __swig_getmethods__["nbin"] = _psrfits_utils.foldinfo_nbin_get
    if _newclass:nbin = _swig_property(_psrfits_utils.foldinfo_nbin_get, _psrfits_utils.foldinfo_nbin_set)
    __swig_setmethods__["tfold"] = _psrfits_utils.foldinfo_tfold_set
    __swig_getmethods__["tfold"] = _psrfits_utils.foldinfo_tfold_get
    if _newclass:tfold = _swig_property(_psrfits_utils.foldinfo_tfold_get, _psrfits_utils.foldinfo_tfold_set)
    def __init__(self): 
        this = _psrfits_utils.new_foldinfo()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _psrfits_utils.delete_foldinfo
    __del__ = lambda self : None;
foldinfo_swigregister = _psrfits_utils.foldinfo_swigregister
foldinfo_swigregister(foldinfo)

class psrfits(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, psrfits, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, psrfits, name)
    __repr__ = _swig_repr
    __swig_setmethods__["basefilename"] = _psrfits_utils.psrfits_basefilename_set
    __swig_getmethods__["basefilename"] = _psrfits_utils.psrfits_basefilename_get
    if _newclass:basefilename = _swig_property(_psrfits_utils.psrfits_basefilename_get, _psrfits_utils.psrfits_basefilename_set)
    __swig_setmethods__["filename"] = _psrfits_utils.psrfits_filename_set
    __swig_getmethods__["filename"] = _psrfits_utils.psrfits_filename_get
    if _newclass:filename = _swig_property(_psrfits_utils.psrfits_filename_get, _psrfits_utils.psrfits_filename_set)
    __swig_setmethods__["N"] = _psrfits_utils.psrfits_N_set
    __swig_getmethods__["N"] = _psrfits_utils.psrfits_N_get
    if _newclass:N = _swig_property(_psrfits_utils.psrfits_N_get, _psrfits_utils.psrfits_N_set)
    __swig_setmethods__["T"] = _psrfits_utils.psrfits_T_set
    __swig_getmethods__["T"] = _psrfits_utils.psrfits_T_get
    if _newclass:T = _swig_property(_psrfits_utils.psrfits_T_get, _psrfits_utils.psrfits_T_set)
    __swig_setmethods__["filenum"] = _psrfits_utils.psrfits_filenum_set
    __swig_getmethods__["filenum"] = _psrfits_utils.psrfits_filenum_get
    if _newclass:filenum = _swig_property(_psrfits_utils.psrfits_filenum_get, _psrfits_utils.psrfits_filenum_set)
    __swig_setmethods__["rownum"] = _psrfits_utils.psrfits_rownum_set
    __swig_getmethods__["rownum"] = _psrfits_utils.psrfits_rownum_get
    if _newclass:rownum = _swig_property(_psrfits_utils.psrfits_rownum_get, _psrfits_utils.psrfits_rownum_set)
    __swig_setmethods__["tot_rows"] = _psrfits_utils.psrfits_tot_rows_set
    __swig_getmethods__["tot_rows"] = _psrfits_utils.psrfits_tot_rows_get
    if _newclass:tot_rows = _swig_property(_psrfits_utils.psrfits_tot_rows_get, _psrfits_utils.psrfits_tot_rows_set)
    __swig_setmethods__["rows_per_file"] = _psrfits_utils.psrfits_rows_per_file_set
    __swig_getmethods__["rows_per_file"] = _psrfits_utils.psrfits_rows_per_file_get
    if _newclass:rows_per_file = _swig_property(_psrfits_utils.psrfits_rows_per_file_get, _psrfits_utils.psrfits_rows_per_file_set)
    __swig_setmethods__["status"] = _psrfits_utils.psrfits_status_set
    __swig_getmethods__["status"] = _psrfits_utils.psrfits_status_get
    if _newclass:status = _swig_property(_psrfits_utils.psrfits_status_get, _psrfits_utils.psrfits_status_set)
    __swig_setmethods__["fptr"] = _psrfits_utils.psrfits_fptr_set
    __swig_getmethods__["fptr"] = _psrfits_utils.psrfits_fptr_get
    if _newclass:fptr = _swig_property(_psrfits_utils.psrfits_fptr_get, _psrfits_utils.psrfits_fptr_set)
    __swig_setmethods__["multifile"] = _psrfits_utils.psrfits_multifile_set
    __swig_getmethods__["multifile"] = _psrfits_utils.psrfits_multifile_get
    if _newclass:multifile = _swig_property(_psrfits_utils.psrfits_multifile_get, _psrfits_utils.psrfits_multifile_set)
    __swig_setmethods__["quiet"] = _psrfits_utils.psrfits_quiet_set
    __swig_getmethods__["quiet"] = _psrfits_utils.psrfits_quiet_get
    if _newclass:quiet = _swig_property(_psrfits_utils.psrfits_quiet_get, _psrfits_utils.psrfits_quiet_set)
    __swig_setmethods__["mode"] = _psrfits_utils.psrfits_mode_set
    __swig_getmethods__["mode"] = _psrfits_utils.psrfits_mode_get
    if _newclass:mode = _swig_property(_psrfits_utils.psrfits_mode_get, _psrfits_utils.psrfits_mode_set)
    __swig_setmethods__["hdr"] = _psrfits_utils.psrfits_hdr_set
    __swig_getmethods__["hdr"] = _psrfits_utils.psrfits_hdr_get
    if _newclass:hdr = _swig_property(_psrfits_utils.psrfits_hdr_get, _psrfits_utils.psrfits_hdr_set)
    __swig_setmethods__["sub"] = _psrfits_utils.psrfits_sub_set
    __swig_getmethods__["sub"] = _psrfits_utils.psrfits_sub_get
    if _newclass:sub = _swig_property(_psrfits_utils.psrfits_sub_get, _psrfits_utils.psrfits_sub_set)
    __swig_setmethods__["fold"] = _psrfits_utils.psrfits_fold_set
    __swig_getmethods__["fold"] = _psrfits_utils.psrfits_fold_get
    if _newclass:fold = _swig_property(_psrfits_utils.psrfits_fold_get, _psrfits_utils.psrfits_fold_set)
    def __init__(self): 
        this = _psrfits_utils.new_psrfits()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _psrfits_utils.delete_psrfits
    __del__ = lambda self : None;
psrfits_swigregister = _psrfits_utils.psrfits_swigregister
psrfits_swigregister(psrfits)


def psrfits_create(*args):
  return _psrfits_utils.psrfits_create(*args)
psrfits_create = _psrfits_utils.psrfits_create

def psrfits_write_subint(*args):
  return _psrfits_utils.psrfits_write_subint(*args)
psrfits_write_subint = _psrfits_utils.psrfits_write_subint

def psrfits_write_polycos(*args):
  return _psrfits_utils.psrfits_write_polycos(*args)
psrfits_write_polycos = _psrfits_utils.psrfits_write_polycos

def psrfits_write_ephem(*args):
  return _psrfits_utils.psrfits_write_ephem(*args)
psrfits_write_ephem = _psrfits_utils.psrfits_write_ephem

def psrfits_close(*args):
  return _psrfits_utils.psrfits_close(*args)
psrfits_close = _psrfits_utils.psrfits_close
SEARCH_MODE = _psrfits_utils.SEARCH_MODE
FOLD_MODE = _psrfits_utils.FOLD_MODE

def psrfits_obs_mode(*args):
  return _psrfits_utils.psrfits_obs_mode(*args)
psrfits_obs_mode = _psrfits_utils.psrfits_obs_mode

def psrfits_remove_polycos(*args):
  return _psrfits_utils.psrfits_remove_polycos(*args)
psrfits_remove_polycos = _psrfits_utils.psrfits_remove_polycos

def psrfits_remove_ephem(*args):
  return _psrfits_utils.psrfits_remove_ephem(*args)
psrfits_remove_ephem = _psrfits_utils.psrfits_remove_ephem

def psrfits_open(*args):
  return _psrfits_utils.psrfits_open(*args)
psrfits_open = _psrfits_utils.psrfits_open

def psrfits_read_subint(*args):
  return _psrfits_utils.psrfits_read_subint(*args)
psrfits_read_subint = _psrfits_utils.psrfits_read_subint

def psrfits_read_part_DATA(*args):
  return _psrfits_utils.psrfits_read_part_DATA(*args)
psrfits_read_part_DATA = _psrfits_utils.psrfits_read_part_DATA

def scale_and_offset_data(*args):
  return _psrfits_utils.scale_and_offset_data(*args)
scale_and_offset_data = _psrfits_utils.scale_and_offset_data

def convert2_float_array(*args):
  return _psrfits_utils.convert2_float_array(*args)
convert2_float_array = _psrfits_utils.convert2_float_array

def print_float_array(*args):
  return _psrfits_utils.print_float_array(*args)
print_float_array = _psrfits_utils.print_float_array

def convert_uchar_array(*args):
  return _psrfits_utils.convert_uchar_array(*args)
convert_uchar_array = _psrfits_utils.convert_uchar_array

def print_uchar_array(*args):
  return _psrfits_utils.print_uchar_array(*args)
print_uchar_array = _psrfits_utils.print_uchar_array

def get_ld(*args):
  return _psrfits_utils.get_ld(*args)
get_ld = _psrfits_utils.get_ld

def set_float_value(*args):
  return _psrfits_utils.set_float_value(*args)
set_float_value = _psrfits_utils.set_float_value


