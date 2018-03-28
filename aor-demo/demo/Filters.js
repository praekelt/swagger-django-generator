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

export const PetFilter = props => (
    <Filter {...props}>
        <Number label="Pet Id" source="pet_id" />
    </Filter>
);

export const UserFilter = props => (
    <Filter {...props}>
        <Number label="User Id" source="user_id" />
    </Filter>
);

/** End of Generated Code **/