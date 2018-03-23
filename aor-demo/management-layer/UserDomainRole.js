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
    DateField,
    TextField,
    NumberInput,
    TextInput,
    DisabledInput,
    DeleteButton,
    EditButton,
    ShowButton
} from 'admin-on-rest';

const validationCreateUserDomainRole = values => {
    const errors = {};
    if (!values.domain_id) {
        errors.domain_id = ["domain_id is required"];
    }
    if (!values.user_id) {
        errors.user_id = ["user_id is required"];
    }
    if (!values.role_id) {
        errors.role_id = ["role_id is required"];
    }
    return errors;
}

export const UserDomainRoleShow = props => (
    <Show {...props} title="UserDomainRole Show">
        <SimpleShowLayout>
            <ReferenceField label="Domain" source="domain_id" reference="domains" allowEmpty>
                <NumberField source="id" />
            </ReferenceField>
            <DateField source="updated_at" />
            <DateField source="created_at" />
            <ReferenceField label="User" source="user_id" reference="users" allowEmpty>
                <TextField source="id" />
            </ReferenceField>
            <ReferenceField label="Role" source="role_id" reference="roles" allowEmpty>
                <NumberField source="id" />
            </ReferenceField>
        </SimpleShowLayout>
    </Show>
)

export const UserDomainRoleCreate = props => (
    <Create {...props} title="UserDomainRole Create">
        <SimpleForm validate={validationCreateUserDomainRole}>
            <ReferenceInput label="Domain" source="domain_id" reference="domains" allowEmpty>
                <SelectInput source="id" />
            </ReferenceInput>
            <ReferenceInput label="User" source="user_id" reference="users" allowEmpty>
                <SelectInput source="id" />
            </ReferenceInput>
            <ReferenceInput label="Role" source="role_id" reference="roles" allowEmpty>
                <SelectInput source="id" />
            </ReferenceInput>
        </SimpleForm>
    </Create>
)

export const UserDomainRoleList = props => (
    <List {...props} title="UserDomainRole List">
        <Datagrid>
            <ReferenceField label="Domain" source="domain_id" reference="domains" allowEmpty>
                <NumberField source="id" />
            </ReferenceField>
            <DateField source="updated_at" />
            <DateField source="created_at" />
            <ReferenceField label="User" source="user_id" reference="users" allowEmpty>
                <TextField source="id" />
            </ReferenceField>
            <ReferenceField label="Role" source="role_id" reference="roles" allowEmpty>
                <NumberField source="id" />
            </ReferenceField>
            <EditButton />
            <ShowButton />
            <DeleteButton />
        </Datagrid>
    </List>
)

