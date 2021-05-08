import { Application } from 'stimulus'
import StimulusReflex from 'stimulus_reflex'
import WebsocketConsumer from 'sockpuppet-js'

import CounterController from './controllers/counter_controller.js'
import TodosController from './controllers/todos_controller'

const application = Application.start()
const consumer = new WebsocketConsumer('ws://localhost:8000/ws/sockpuppet-sync')

application.register('counter', CounterController)
application.register('todos', TodosController)

StimulusReflex.initialize(application, { consumer })
