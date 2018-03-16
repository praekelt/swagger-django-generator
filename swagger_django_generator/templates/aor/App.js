import React from 'react';
import { simpleRestClient, Admin, Resource } from 'admin-on-rest';
import { Delete } from 'admin-on-rest/lib/mui';

{% for name, actions in resources.items() %}
import { 
{% if actions.list_show %}    {{ actions.list_show.list_component }},
    {{ actions.list_show.show_component }}{% endif %}{% if actions.create %},
    {{ actions.create.component }}{% endif %}{% if actions.edit %},
    {{ actions.edit.component }}{% endif %}

} from './{{ name }}';
{% endfor %}


const App = () => (
    <Admin title={"{{ title }}"} restClient={simpleRestClient}>
    {% for name, actions in resources.items() %}
        <Resource
            name={"{{ name }}"}
            {% if actions.list_show %}
            list={ {{ actions.list_show.list_component }} }
            show={ {{ actions.list_show.show_component }} }
            {% endif %}
            {% if actions.create %}
            create={ {{ actions.create.component }} }
            {% endif %}
            {% if actions.edit %}
            edit={ {{ actions.edit.component }}}
            {% endif %}
            remove={Delete}
        />
    {% endfor %}
    </Admin>
)

export default App;