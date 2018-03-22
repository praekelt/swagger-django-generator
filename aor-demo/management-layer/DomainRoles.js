import React from 'react';
import {
    List,
    Show,
    Edit,
    Create,
    Datagrid,
    SimpleShowLayout,
    SimpleForm,
    NumberField,
    DisabledInput,
    EditButton

} from 'admin-on-rest';

export const DomainRolesList = props => (
    <List {...props} title="DomainRoles List">
        <Datagrid>
            <NumberField source="domain_id" />
        </Datagrid>
    </List>
)

export const DomainRolesShow = props => (
    <Show {...props} title="DomainRoles Show">
        <SimpleShowLayout>
            <NumberField source="domain_id" />
        </SimpleShowLayout>
    </Show>
)

