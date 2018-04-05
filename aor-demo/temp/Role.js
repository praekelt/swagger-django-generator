/**
 * Generated Role.js code. Edit at own risk.
 * When regenerated the changes will be lost.
**/
import React from 'react';
import {
    List,
    Datagrid,
    NumberField,
    TextField,
    BooleanField,
    DateField,
    SimpleForm,
    Create,
    TextInput,
    BooleanInput,
    Show,
    SimpleShowLayout,
    ReferenceManyField,
    ReferenceField,
    Edit,
    DeleteButton,
    EditButton,
    ShowButton
} from 'admin-on-rest';
import {
    RoleFilter
} from './Filters';

const validationCreateRole = values => {
    const errors = {};
    if (!values.label) {
        errors.label = ["label is required"];
    }
    if (!values.requires_2fa) {
        errors.requires_2fa = ["requires_2fa is required"];
    }
    return errors;
}

const validationEditRole = values => {
    const errors = {};
    return errors;
}

export const RoleList = props => (
    <List {...props} title="Role List" filters={<RoleFilter />}>
        <Datagrid>
            <NumberField source="id" />
            <TextField source="label" />
            <BooleanField source="requires_2fa" />
            <TextField source="description" />
            <DateField source="created_at" />
            <DateField source="updated_at" />
            <EditButton />
            <ShowButton />
            <DeleteButton />
        </Datagrid>
    </List>
)

export const RoleCreate = props => (
    <Create {...props} title="Role Create">
        <SimpleForm validate={validationCreateRole}>
            <TextInput source="label" />
            <BooleanInput source="requires_2fa" />
            <TextInput source="description" />
        </SimpleForm>
    </Create>
)

export const RoleShow = props => (
    <Show {...props} title="Role Show">
        <SimpleShowLayout>
            <NumberField source="id" />
            <TextField source="label" />
            <BooleanField source="requires_2fa" />
            <TextField source="description" />
            <DateField source="created_at" />
            <DateField source="updated_at" />
            <ReferenceManyField label="Resource Permissions" reference="roleresourcepermissions" target="role_id">
                <Datagrid>
                    <ReferenceField label="Resource" source="resource_id" reference="resources" linkType="show" allowEmpty>
                        <NumberField source="urn" />
                    </ReferenceField>
                    <ReferenceField label="Permission" source="permission_id" reference="permissions" linkType="show" allowEmpty>
                        <NumberField source="name" />
                    </ReferenceField>
                    <DateField source="created_at" />
                    <DateField source="updated_at" />
                </Datagrid>
            </ReferenceManyField>
        </SimpleShowLayout>
    </Show>
)

export const RoleEdit = props => (
    <Edit {...props} title="Role Edit">
        <SimpleForm validate={validationEditRole}>
            <TextInput source="label" />
            <BooleanInput source="requires_2fa" />
            <TextInput source="description" />
            <ReferenceManyField label="Resource Permissions" reference="roleresourcepermissions" target="role_id">
                <Datagrid>
                    <ReferenceField label="Resource" source="resource_id" reference="resources" linkType="show" allowEmpty>
                        <NumberField source="urn" />
                    </ReferenceField>
                    <ReferenceField label="Permission" source="permission_id" reference="permissions" linkType="show" allowEmpty>
                        <NumberField source="name" />
                    </ReferenceField>
                    <DateField source="created_at" />
                    <DateField source="updated_at" />
                    <EditButton />
                </Datagrid>
            </ReferenceManyField>
        </SimpleForm>
    </Edit>
)

/** End of Generated Code **/