from django.db import models
from datetime import date

# Create your models here.

class Mycv(models.Model):
    DEFAULT_ID_CV = 1
    pass

class Experience(models.Model):
    position = models.CharField(max_length=200, blank=True, default="Software Developer")
    company = models.CharField(max_length=200, blank=True, default="Google")
    location = models.CharField(max_length=200, blank=False, default="Madrid, Spain")
    startdate = models.DateField(auto_now=False, auto_now_add=False, blank=True, default=date.today)
    finaldate = models.DateField(auto_now=False, auto_now_add=True, blank=False, null=True)
    description = models.TextField(blank=False, default="My Job description")
    cv_experience = models.ForeignKey(Mycv, on_delete=models.CASCADE, default=Mycv.DEFAULT_ID_CV)

    def __str__(self):
        return self.position + " .- " + self.company + " -. " + self.location + " (" + self.startdate.__str__() + " - " + self.finaldate.__str__() + ")"

class Education(models.Model):
    university = models.CharField(max_length=200, blank=True, default="Oxford University")
    certification = models.CharField(max_length=200, blank=False, default="Software Engineer")
    academic_discipline = models.CharField(max_length=200, blank=False, default="Software Engineer") # In the future make a CHOICE
    mark = models.DecimalField(max_digits=3, decimal_places=2, blank=False, null=True, default=5.55)  # x.xx
    description = models.TextField(max_length=200, blank=False, default="My education description")
    startdate = models.DateField(auto_now=False, auto_now_add=False, blank=True, default=date.today)
    finaldate = models.DateField(auto_now=False, auto_now_add=True, blank=False, null=True)
    activities = models.TextField(max_length=200, blank=False, default="Football Team & Choir") 
    cv_education = models.ForeignKey(Mycv, on_delete=models.CASCADE, default=Mycv.DEFAULT_ID_CV)

    def __str__(self):
        return self.university + " - " + self.certification + " .- (" + self.mark.__str__() + ") -. " + self.academic_discipline + " (" + self.startdate.__str__() + " - " + self.finaldate.__str__() + ")"

# FOREIGN KEY TEST
# ------------------
#### Cv Create
# cv = Mycv()
# cv.save()

#### 2 experiences created
# exp = Experience()
# exp.save()  # By default this assign to Mycv with id = 1 (The first one)
# exp2 = Experience()
# exp2

#### Show all Experiences
# Experience.objects.all()

#### Show the Cv associated experiences
# cv.experience_set.all() 
# <QuerySet [<Experience: Software Developer .- Google -. Madrid, Spain (2018-08-07 - 2018-08-07)>, <Experience: Software Developer .- Google -. Madrid, Spain (2018-08-07 - 2018-08-07)>]>

#### Cv Deleted output (Cascade)
# cv.delete()
# (3, {'cv.Experience': 1, 'cv.Education': 1, 'cv.Mycv': 1})
# ------------------

# List of Methods Models
# 1. __str__()
#     return string representation of an object

# 2. def save(self, *args, **kwargs):
#         do_something()
#         super().save(*args, **kwargs)  # Call the "real" save() method.
#         do_something_else()
# 3. get_absolute_url()
# 4. @property
#     def full_name(self):
#         "Returns the person's full name."
#        return '%s %s' % (self.first_name, self.last_name)
# 5. @classmethod
#     def from_db(cls, db, field_names, values):
#         if len(values) != len(cls._meta.concrete_fields):
#             values_iter = iter(values)
#             values = [
#                 next(values_iter) if f.attname in field_names else DEFERRED
#                 for f in cls._meta.concrete_fields
#             ]
#         new = cls(*values)
#         new._state.adding = False
#         new._state.db = db
#         return new


# 6. def __repr__(self):
#         return '<%s: %s>' % (self.__class__.__name__, self)

# 8. def __eq__(self, other):
#         if not isinstance(other, Model):
#             return False
#         if self._meta.concrete_model != other._meta.concrete_model:
#             return False
#         my_pk = self.pk
#         if my_pk is None:
#             return self is other
#         return my_pk == other.pk


# 9. def __hash__(self):
#         if self.pk is None:
#             raise TypeError("Model instances without primary key value are unhashable")
#         return hash(self.pk)


# 10. def __reduce__(self):
#         data = self.__getstate__()
#         data[DJANGO_VERSION_PICKLE_KEY] = get_version()
#         class_id = self._meta.app_label, self._meta.object_name
#         return model_unpickle, (class_id,), data

# 11. def __getstate__(self):
#         """Hook to allow choosing the attributes to pickle."""
#         return self.__dict__

# 12. def __setstate__(self, state):
#         msg = None
#         pickled_version = state.get(DJANGO_VERSION_PICKLE_KEY)
#         if pickled_version:
#             current_version = get_version()
#             if current_version != pickled_version:
#                 msg = (
#                     "Pickled model instance's Django version %s does not match "
#                     "the current version %s." % (pickled_version, current_version)
#                 )
#         else:
#             msg = "Pickled model instance's Django version is not specified."

#         if msg:
#             warnings.warn(msg, RuntimeWarning, stacklevel=2)

#         self.__dict__.update(state)

# 13. def _get_pk_val(self, meta=None):
#         if not meta:
#             meta = self._meta
#         return getattr(self, meta.pk.attname)

# 14. def _set_pk_val(self, value):
#         return setattr(self, self._meta.pk.attname, value)

#     pk = property(_get_pk_val, _set_pk_val)

# 15. def get_deferred_fields(self):
#         """
#         Return a set containing names of deferred fields for this instance.
#         """
#         return {
#             f.attname for f in self._meta.concrete_fields
#             if f.attname not in self.__dict__
#         }