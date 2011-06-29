from piston.utils import Mimer
from piston.emitters import Emitter
from piston.doc import generate_doc

from restful.emitters import HTMLEmitter

#from story.api.handlers import StoryHandler 
#from project.api.handlers import ProjectHandler, ReleaseHandler 

#register emitter
Emitter.register('html', HTMLEmitter, 'text/html; charset=utf-8')

#register content-type 
Mimer.register(lambda *a: None, ('text/plain',))

#register document
#docs = [generate_doc(StoryHandler), generate_doc(ReleaseHandler), generate_doc(ProjectHandler)]
