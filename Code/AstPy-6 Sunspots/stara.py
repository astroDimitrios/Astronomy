import astropy.units as u
import numpy as np
from skimage.filters import median
from skimage.morphology import disk, square, white_tophat
from skimage.util import invert
import sunpy.map


@u.quantity_input
def stara(smap, circle_radius: u.deg = 100*u.arcsec, median_box: u.deg = 10*u.arcsec,
          threshold=6000, limb_filter: u.percent = None):
    """
    A method for automatically detecting sunspots in white-light data using morphological operations.
    Parameters
    ----------
    smap : `sunpy.map.GenericMap`
        The map to apply the algorithm to.
    circle_radius : `astropy.units.Quantity`, optional
        The angular size of the structuring element used in the
        `skimage.morphology.white_tophat`. This is the maximum radius of
        detected features.
    median_box : `astropy.units.Quantity`, optional
        The size of the structuring element for the median filter, features
        smaller than this will be averaged out.
    threshold : `int`, optional
        The threshold used for detection, this will be subject to detector
        degradation. The default is a reasonable value for HMI continuum images.
    limb_filter : `astropy.units.Quantity`, optional
        If set, ignore features close to the limb within a percentage of the
        radius of the disk. A value of 10% generally filters out false
        detections around the limb with HMI continuum images.
    """
    data = invert(smap.data)

    # Filter things that are close to limb to reduce false detections
    if limb_filter is not None:
        hpc_coords = sunpy.map.all_coordinates_from_map(smap)
        r = np.sqrt(hpc_coords.Tx ** 2 + hpc_coords.Ty ** 2) / (smap.rsun_obs - smap.rsun_obs * limb_filter)
        data[r > 1] = np.nan

    # Median filter to remove detections based on hot pixels
    m_pix = int((median_box / smap.scale[0]).to_value(u.pix))
    med = median(data, square(m_pix), behavior="ndimage")

    # Construct the pixel structuring element
    c_pix = int((circle_radius / smap.scale[0]).to_value(u.pix))
    circle = disk(c_pix / 2)

    finite = white_tophat(med, circle)
    finite[np.isnan(finite)] = 0  # Filter out nans

    return finite > threshold