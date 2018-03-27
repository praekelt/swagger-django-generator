/** 
 * Generated Filters.js code. Edit at own risk.
 * When regenerated the changes will be lost.
**/
import React from 'react';
import {
    Filter,
    TextInput,
    NumberInput,
    BooleanInput
} from 'admin-on-rest';

{% for name, resource in resources.items() %}
{% if resource.filters %}
export const {{ resource.title }}Filter = props => (
    <Filter {...props}>
        {% for filter in resource.filters %}
        <{{ filter.component }} label="{{ filter.label }}" source="{{ filter.source }}" />
        {% endfor %}
    </Filter>
);

{% endif %}
{% endfor %}
/** End of Generated Code **/