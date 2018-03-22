import React from 'react';
import {
    List,
    Show,
    Edit,
    Create,
    Datagrid,
    SimpleShowLayout,
    SimpleForm,
    TextField,
    DisabledInput,
    EditButton

} from 'admin-on-rest';

export const AllUserRolesList = props => (
    <List {...props} title="AllUserRoles List">
        <Datagrid>
            <TextField source="user_id" />
        </Datagrid>
    </List>
)

export const AllUserRolesShow = props => (
    <Show {...props} title="AllUserRoles Show">
        <SimpleShowLayout>
            <TextField source="user_id" />
        </SimpleShowLayout>
    </Show>
)

