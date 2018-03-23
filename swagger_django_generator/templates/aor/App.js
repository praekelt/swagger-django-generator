import React from 'react';
import { simpleRestClient, Admin, Resource } from 'admin-on-rest';
import { Delete } from 'admin-on-rest/lib/mui';

{% for name, actions in resources.items() %}
{% if actions.has_methods %}
import {
    {% for action, details in actions.items() %}
    {% if action in supported_components %}
    {{ actions.title }}{{ action|title }},
    {% endif %}
    {% endfor %}
} from './{{ actions.title }}';

{% endif %}
{% endfor %}


const App = () => (
    <Admin title={"{{ title }}"} restClient={simpleRestClient}>
    {% for name, actions in resources.items() %}
    {% if actions.has_methods %}
        <Resource
            name="{{ actions.path }}"
            {% for action, details in actions.items() %}
            {% if action in supported_components %}
            {{ action }}={ {{ actions.title }}{{ action|title }} }
            {% endif %}
            {% endfor %}
            remove={Delete}
        />
    {% endif %}
    {% endfor %}
    </Admin>
)

export default App;