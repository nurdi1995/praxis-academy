from __future__ import (
    absolute_import,
    unicode_literals
)

class CRC(object):  #

    def __init__(self, name, kind="class",
                    collaborators=None,
                    responsibilities=None):
        self.name = name
        self.kind = kind
        self.collaborators = collaborators or []
        self.responsibilities = responsibilities or []

    def __repr__(self):
        tempalate = (
            '{class_}{name},',
            'kind={kind},',
            'collaborators={collaborators},',
            'responsibilities= {rsponsibilities})'
        )    

        return ''.join(tempalate).format(
            class_=self.__class__.__name__,
            name = self.name,
            kind = self.kind,
            collaborators = self.collaborators,
            responsibilities=self.responsibilities
        )

        def to_dict(self):
            #fungsi yang merepresemnasikan instance attribut
            return {
                'name': self.name,
                'kind': self.kind,
                'colaborators' : self.collaborators,
                'responsibilities': self.responsibilities
                
            }
    
    