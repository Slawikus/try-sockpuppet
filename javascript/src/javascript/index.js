import { Application } from 'stimulus'
import StimulusReflex from 'stimulus_reflex'
import WebsocketConsumer from 'sockpuppet-js'

import CounterController from './controllers/counter_controller.js'

const application = Application.start()
const consumer = new WebsocketConsumer('ws://localhost:8000/ws/sockpuppet-sync')

application.register('counter', CounterController)
StimulusReflex.initialize(application, { consumer })
