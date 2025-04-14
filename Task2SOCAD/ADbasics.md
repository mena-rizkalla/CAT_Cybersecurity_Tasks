# Microsoft Active Directory: A Summary

Microsoft's Active Directory (AD) is a cornerstone of enterprise IT infrastructure. It's a directory service that centralizes the management of users, computers, and other network resources. This centralization simplifies network administration and enhances security.

## The Need for Active Directory

In a small network, managing a few computers and users might be manageable manually. However, as organizations grow, this becomes increasingly complex.:

> you can't manage 157 computes and 320 different users located across four different offices so we use a Windows domain

This is where AD comes in.

## Windows Domains and Domain Controllers

A Windows domain is a logical group of users and computers that share a common directory database and security policies. It provides a framework for centralized administration.

The core idea is to centralize the administration of network resources in a single repository: Active Directory.

A Domain Controller (DC) is a server that runs the Active Directory Domain Services (AD DS) role. It stores and manages the directory data.

## Real-World Example

how AD is used in a school or university:

> In school/university networks, you will often be provided with a username and password that you can use on any of the computers available on campus. Your credentials are valid for all machines because whenever you input them on a machine, it will forward the authentication process back to the Active Directory, where your credentials will be checked. Thanks to Active Directory, your credentials don't need to exist in each machine and are available throughout the network.

> Active Directory is also the component that allows your school/university to restrict you from accessing the control panel on your school/university machines. Policies will usually be deployed throughout the network so that you don't have administrative privileges over those computers.

This highlights two key benefits of AD:

* **Single Sign-On (SSO):** Users can log in once and access multiple resources.
* **Centralized Policy Management:** Administrators can enforce consistent configurations and restrictions across the network.

## Active Directory Domain Services (AD DS)

The core of any Windows Domain is the Active Directory Domain Service (AD DS). Key functions of AD DS include:

* **Directory Service:** Stores information about network resources (objects).
* **Centralized Authentication:** Verifies user credentials.
* **Authorization:** Determines what resources users can access.

## Objects in Active Directory

AD DS organizes network resources as objects. Here are some common object types:

* **Users:**
    * Represent individuals (employees, students, etc.).
    * Can also represent services (e.g., for applications like IIS or databases like MSSQL).
* **Computers:**
    * Every computer that joins a domain becomes an object in AD.
    * Machine accounts are created for computers (e.g., DC01$).
* **Groups:**
    * Used to organize users and computers, simplifying permission management.
    * Security groups are used to assign permissions.
    * Common security groups include:

        | Security Group              | Description                                                 |
        | :-------------------------- | :---------------------------------------------------------- |
        | Domain Admins               | Full administrative control over the entire domain.         |
        | Enterprise Admins           | Full administrative control over the entire forest.         |
        | Server Operators            | Can administer domain controllers.                          |
        | Backup Operators            | Can bypass file permissions to back up data.                |
        | Account Operators           | Can create and modify user and group accounts.              |
        | Domain Users                | All regular user accounts in the domain.                    |
        | Domain Computers            | All computer accounts in the domain.                        |
        | Domain Controllers          | All domain controllers in the domain.                       |
        | Group Policy Creator Owners | Members can change group policy.                            |
        | Read-only Domain Controllers | Can administer domain controllers.                          |

## Active Directory Administrative Tools

* **Active Directory Users and Computers (ADUC):** The primary tool for managing users, groups, computers, and organizational units (OUs). It is typically run on a Domain Controller.

## Organizational Units (OUs)

OUs are containers within a domain that help organize objects (users, groups, computers) into a hierarchical structure.

OUs are used to:

* Reflect the organization's structure (e.g., departments, locations).
* Simplify administration.
* Delegate administrative control.
* Apply Group Policies.

Default OUs include:

* Builtin: Default groups.
* Computers: Where computers are placed by default when joining the domain.
* Domain Controllers: Contains the domain controllers.
* Users: Default location for user accounts.
* Managed Service Accounts: Holds accounts used by services.

## Delegation of Control

Delegation allows administrators to grant specific permissions to users or groups over specific OUs. This enables distributed administration without requiring full Domain Admin privileges.

## Group Policy

Group Policy Objects (GPOs) are collections of settings that define the desired configuration for users and computers.

GPOs can be linked to domains, sites, or OUs.

GPOs are used to enforce a wide range of settings, including:

* Password policies
* Software installation
* Desktop configuration
* Security settings

The Group Policy Management tool is used to create and manage GPOs.

GPOs are stored in the SYSVOL shared folder on domain controllers (typically `C:\Windows\SYSVOL\sysvol\`). Clients access SYSVOL to retrieve GPOs.

GPO changes can take up to 2 hours to propagate. The `gpupdate /force` command can be used to immediately update GPOs on a client:

```powershell
PS C:\> gpupdate /force
```


# Active Directory Authentication and Forests

## Authentication Protocols

Active Directory primarily utilizes two authentication protocols:

* **Kerberos:**
    * The default and preferred protocol for modern Windows operating systems.
    * Relies on the use of tickets to verify user and computer identities.

* **NTLM (NT LAN Manager):**
    * A legacy authentication protocol.
    * Mainly retained for backward compatibility with older systems.
    * Considered less secure compared to Kerberos.

## Forests

* A forest represents a logical grouping of one or more domain trees.
* Domains within the same forest share several key aspects:
    * **Common Schema:** A unified definition of objects and their attributes across the forest.
    * **Common Configuration:** Shared configuration settings that apply forest-wide.
    * **Global Catalog:** A searchable index of all objects within the forest, facilitating efficient lookups.
* Forests provide a mechanism for organizations to expand their Active Directory infrastructure across multiple distinct domains.
* This allows for scalability even when individual domains have different naming conventions or are managed independently.

**Example:**

Consider a scenario where your company expands and acquires "MHT Inc." Post-merger, each company might retain its existing domain structure and IT department. To integrate these separate domain trees with potentially different naming schemes into a unified network, you would establish an Active Directory **forest**. This allows resources and users across both former companies to interact within a single, trust-based environment.

---
*This summary provides a concise overview of Active Directory authentication protocols and the concept of forests.*
