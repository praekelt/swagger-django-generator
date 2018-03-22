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
    TextField,
    DisabledInput,
    EditButton

} from 'admin-on-rest';

export const UserSiteRoleLabelsAggregatedList = props => (
    <List {...props} title="UserSiteRoleLabelsAggregated List">
        <Datagrid>
            <NumberField source="site_id" />
            <TextField source="user_id" />
        </Datagrid>
    </List>
)

export const UserSiteRoleLabelsAggregatedShow = props => (
    <Show {...props} title="UserSiteRoleLabelsAggregated Show">
        <SimpleShowLayout>
            <NumberField source="site_id" />
            <TextField source="user_id" />
        </SimpleShowLayout>
    </Show>
)

