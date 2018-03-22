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

export const SiteAndDomainRolesList = props => (
    <List {...props} title="SiteAndDomainRoles List">
        <Datagrid>
            <NumberField source="site_id" />
        </Datagrid>
    </List>
)

export const SiteAndDomainRolesShow = props => (
    <Show {...props} title="SiteAndDomainRoles Show">
        <SimpleShowLayout>
            <NumberField source="site_id" />
        </SimpleShowLayout>
    </Show>
)

