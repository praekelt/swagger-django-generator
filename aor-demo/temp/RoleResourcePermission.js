/**
 * Generated RoleResourcePermission.js code. Edit at own risk.
 * When regenerated the changes will be lost.
**/
import React from 'react';
import {
    List,
    Datagrid,
    ReferenceField,
    NumberField,
    DateField,
    SimpleForm,
    Create,
    ReferenceInput,
    SelectInput,
    Show,
    SimpleShowLayout,
    DisabledInput,
    DeleteButton,
    EditButton,
    ShowButton
} from 'admin-on-rest';
import {
    RoleResourcePermissionFilter
} from './Filters';

const validationCreateRoleResourcePermission = values => {
    const errors = {};
    if (!values.role_id) {
        errors.role_id = ["role_id is required"];
    }
    if (!values.resource_id) {
        errors.resource_id = ["resource_id is required"];
    }
    if (!values.permission_id) {
        errors.permission_id = ["permission_id is required"];
    }
    return errors;
}

export const RoleResourcePermissionList = props => (
    <List {...props} title="RoleResourcePermission List" filters={<RoleResourcePermissionFilter />}>
        <Datagrid>
            <ReferenceField label="Role" source="role_id" reference="roles" linkType="show" allowEmpty>
                <NumberField source="label" />
            </ReferenceField>
            <ReferenceField label="Resource" source="resource_id" reference="resources" linkType="show" allowEmpty>
                <NumberField source="urn" />
            </ReferenceField>
            <ReferenceField label="Permission" source="permission_id" reference="permissions" linkType="show" allowEmpty>
                <NumberField source="name" />
            </ReferenceField>
            <DateField source="created_at" />
            <DateField source="updated_at" />
            <EditButton />
            <ShowButton />
            <DeleteButton />
        </Datagrid>
    </List>
)

export const RoleResourcePermissionCreate = props => (
    <Create {...props} title="RoleResourcePermission Create">
        <SimpleForm validate={validationCreateRoleResourcePermission}>
            <ReferenceInput label="Role" source="role_id" reference="roles" allowEmpty>
                <SelectInput source="id" optionText="label" />
            </ReferenceInput>
            <ReferenceInput label="Resource" source="resource_id" reference="resources" allowEmpty>
                <SelectInput source="id" optionText="urn" />
            </ReferenceInput>
            <ReferenceInput label="Permission" source="permission_id" reference="permissions" allowEmpty>
                <SelectInput source="id" optionText="name" />
            </ReferenceInput>
        </SimpleForm>
    </Create>
)

export const RoleResourcePermissionShow = props => (
    <Show {...props} title="RoleResourcePermission Show">
        <SimpleShowLayout>
            <ReferenceField label="Role" source="role_id" reference="roles" linkType="show" allowEmpty>
                <NumberField source="label" />
            </ReferenceField>
            <ReferenceField label="Resource" source="resource_id" reference="resources" linkType="show" allowEmpty>
                <NumberField source="urn" />
            </ReferenceField>
            <ReferenceField label="Permission" source="permission_id" reference="permissions" linkType="show" allowEmpty>
                <NumberField source="name" />
            </ReferenceField>
            <DateField source="created_at" />
            <DateField source="updated_at" />
        </SimpleShowLayout>
    </Show>
)

/** End of Generated Code **/