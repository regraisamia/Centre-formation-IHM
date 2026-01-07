# Ajout au fichier models.py

class Formation(models.Model):
    """
    Une formation est un programme d'études complet (ex: Développement Web, Marketing Digital)
    Une formation peut avoir plusieurs classes (groupes d'étudiants)
    """
    __tablename__ = 'Formation'
    
    name = models.CharField(_('Nom de la formation'), max_length=100)
    description = models.TextField(_('Description'), blank=True)
    duration_months = models.IntegerField(_('Durée en mois'), default=6)
    price = models.DecimalField(_('Prix'), max_digits=10, decimal_places=2, default=0)
    max_students = models.IntegerField(_('Capacité maximum'), default=25)
    is_active = models.BooleanField(_('Active'), default=True)
    subjects = models.ManyToManyField('Subjects', related_name='formations', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_total_students(self):
        return sum(classe.student_classe.count() for classe in self.classes.all())
    
    def get_completion_rate(self):
        # Logique pour calculer le taux de réussite
        return 85  # Exemple
    
    class Meta:
        verbose_name = _('Formation')
        verbose_name_plural = _('Formations')
        ordering = ['name']