import React from 'react';
import {
    List,
    Show,
    Edit,
    Create,
    Datagrid,
    SimpleShowLayout,
    SimpleForm,
    DateField,
    DateInput,
    NumberField,
    NumberInput,
    DisabledInput,
    EditButton

} from 'admin-on-rest';

const validationCreateRoleResourcePermission = values => {
    const errors = {};
    if (!values.permission_id) {
        errors.permission_id = ["permission_id is required"];
    }
    if (!values.role_id) {
        errors.role_id = ["role_id is required"];
    }
    if (!values.resource_id) {
        errors.resource_id = ["resource_id is required"];
    }
    return errors;
}

export const RoleResourcePermissionList = props => (
    <List {...props} title="RoleResourcePermission List">
        <Datagrid>
            <DateField source="updated_at" />
            <NumberField source="permission_id" />
            <NumberField source="role_id" />
            <DateField source="created_at" />
            <NumberField source="resource_id" />
        </Datagrid>
    </List>
)

export const RoleResourcePermissionShow = props => (
    <Show {...props} title="RoleResourcePermission Show">
        <SimpleShowLayout>
            <DateField source="updated_at" />
            <NumberField source="permission_id" />
            <NumberField source="role_id" />
            <DateField source="created_at" />
            <NumberField source="resource_id" />
        </SimpleShowLayout>
    </Show>
)

export const RoleResourcePermissionCreate = props => (
    <Create {...props} title="Create RoleResourcePermission">
        <SimpleForm validate={validationCreateRoleResourcePermission}>
            <NumberInput source="permission_id" />
            <NumberInput source="role_id" />
            <NumberInput source="resource_id" />
        </SimpleForm>
    </Create>
)

