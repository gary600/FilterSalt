# -*- coding: utf-8 -*-
"""
/***************************************************************************
 FilterSalt
                                 A QGIS plugin
 Filters out "salt and pepper" contour lines
                             -------------------
        begin                : 2017-07-02
        copyright            : (C) 2017 by Gary B
        email                : gpbailey01@bvsd.org
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load FilterSalt class from file FilterSalt.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .FilterSalt import FilterSalt
    return FilterSalt(iface)
