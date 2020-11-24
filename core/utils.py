from hashlib import md5
from datetime import date, datetime
from pytils.translit import slugify


def image_path(instance, filename):
    """
    Returns a file path where to save a photo
    """
    ext = filename.rsplit('.')[-1].lower()
    s = slugify(filename) + '%s' % datetime.now()
    hash = md5(s.encode('utf-8'))
    new_filename = '%s.%s' % (hash.hexdigest()[3:10], ext)

    return u'upload/%s/%d/%d/%s' % (date.today().year, date.today().month,
                                    date.today().day, new_filename)
