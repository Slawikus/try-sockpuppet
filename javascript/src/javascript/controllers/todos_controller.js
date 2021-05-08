import { Controller } from 'stimulus';
import StimulusReflex from 'stimulus_reflex';

export default class extends Controller {
  connect() {
    StimulusReflex.register(this)
  }

  addTodo(event) {
    event.preventDefault()
    this.stimulate('TodoReflex#add_todo', 1)
  }
}
